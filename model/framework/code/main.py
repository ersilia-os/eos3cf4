import os
import sys
import csv
import json
import struct
from pathlib import Path
import warnings
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
from transformers.utils import logging as hf_logging

warnings.filterwarnings("ignore")
hf_logging.set_verbosity_error()


def get_paths():
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  root = Path(__file__).parent.parent.parent
  model_dir = root / "checkpoints" / "models" / "chemgpt-4_7M"
  store_dir = root / "checkpoints" / "models" / "molfeat_store"
  os.makedirs(store_dir, exist_ok=True)
  os.environ.setdefault("MOLFEAT_MODEL_STORE_BUCKET", str(store_dir))
  os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
  return input_file, output_file, model_dir


def read_smiles_csv(p):
  with open(p, "r") as f:
    r = csv.reader(f)
    cols = next(r)
    data = [row[0] for row in r]
  return cols, data


def read_smiles_bin(p):
  with open(p, "rb") as f:
    data = f.read()
  mv = memoryview(data)
  nl = mv.tobytes().find(b"\n")
  meta = json.loads(mv[:nl].tobytes().decode("utf-8"))
  cols = meta.get("columns", [])
  n = meta.get("count", 0)
  out = [None] * n
  off = nl + 1
  for i in range(n):
    (L,) = struct.unpack_from(">I", mv, off)
    off += 4
    out[i] = mv[off : off + L].tobytes().decode("utf-8")
    off += L
  return cols, out


def read_smiles(p):
  return read_smiles_bin(p) if p.endswith(".bin") else read_smiles_csv(p)


def write_csv(arr, header, p):
  with open(p, "w") as f:
    w = csv.writer(f)
    w.writerow(header)
    for row in arr:
      w.writerow(row)


def write_bin(arr, header, p):
  a = np.asarray(arr, dtype=np.float32)
  meta = {"columns": header, "shape": a.shape, "dtype": "float32"}
  b = (json.dumps(meta) + "\n").encode("utf-8")
  with open(p, "wb") as f:
    f.write(b)
    f.truncate(len(b) + a.nbytes)
  m = np.memmap(p, dtype=a.dtype, mode="r+", offset=len(b), shape=a.shape)
  m[:] = a
  m.flush()


def write_out(arr, header, p):
  if p.endswith(".bin"):
    write_bin(arr, header, p)
  elif p.endswith(".csv"):
    write_csv(arr, header, p)
  else:
    raise ValueError(p)


def batcher(x, bs):
  for i in range(0, len(x), bs):
    yield x[i : i + bs]


def prepare_tokenizer(model_dir):
  tok = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
  if tok.pad_token_id is None:
    if getattr(tok, "eos_token_id", None) is not None:
      tok.pad_token = tok.eos_token
      tok.pad_token_id = tok.eos_token_id
    else:
      tok.pad_token_id = 0
  return tok


def load_model(model_dir, device):
  m = AutoModel.from_pretrained(model_dir, local_files_only=True)
  m.eval().to(device)
  return m


def pool_mean(hidden, mask):
  x = hidden * mask.unsqueeze(-1)
  s = x.sum(dim=1)
  l = mask.sum(dim=1, keepdim=True).clamp(min=1)
  return s / l


def embed_smiles(smiles, tok, model, max_len, bs=32, normalize=False, device="cpu"):
  out = []
  with torch.no_grad():
    for chunk in batcher(smiles, bs):
      enc = tok(
        chunk, padding=True, truncation=True, max_length=max_len, return_tensors="pt"
      )
      enc = {k: v.to(device) for k, v in enc.items()}
      y = model(**enc)
      h = y.last_hidden_state
      z = pool_mean(h, enc["attention_mask"])
      if normalize:
        z = torch.nn.functional.normalize(z, p=2, dim=1)
      out.append(z.cpu().numpy().astype(np.float32))
  return np.concatenate(out, axis=0)


def header_from_dim(d):
  return [f"dim_{i:03d}" for i in range(d)]


def main():
  input_file, output_file, model_dir = get_paths()
  _, smiles = read_smiles(input_file)
  device = torch.device("cpu")
  tok = prepare_tokenizer(model_dir)
  model = load_model(model_dir, device)
  max_len = (
    getattr(model.config, "n_positions", None)
    or getattr(model.config, "max_position_embeddings", 512)
    or 512
  )
  embs = embed_smiles(
    smiles, tok, model, max_len, bs=32, normalize=False, device=device
  )
  header = header_from_dim(int(embs.shape[1]))
  write_out(embs, header, output_file)


if __name__ == "__main__":
  main()
