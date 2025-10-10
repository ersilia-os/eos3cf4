---
tags: 
- chemistry
---

# ChemGPT 4.7M
ChemGPT is based on the GPT-Neo model and was introduced in the paper [Neural Scaling of Deep Chemical Models](https://chemrxiv.org/engage/chemrxiv/article-details/627bddd544bdd532395fb4b5).

## Model description
ChemGPT is a transformers model for generative molecular modeling, which was pretrained on the PubChem10M dataset.

## Intended uses & limitations

### How to use
You can use this model directly from the 🤗/transformers library.

### Limitations and bias
This model was trained on a subset of molecules from PubChem. You can use this model to generate molecules, but it is mostly intended to be used for investigations of the effects of pre-training and fine-tuning on downstream datasets.

## Training data
PubChem10M, a dataset of SMILES strings from PubChem, available via [DeepChem](https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/pubchem_10m.txt.zip).

## Training procedure

### Preprocessing
SMILES strings were converted to SELFIES using version 1.0.4 of the SELFIES library.


### Pretraining
See code in the [LitMatter repository](https://github.com/ncfrey/litmatter/blob/main/lit_models/lit_chemgpt.py).

### BibTeX entry and citation info
```
@article{frey_soklaski_axelrod_samsi_gomez-bombarelli_coley_gadepally_2022, 
place={Cambridge}, title={Neural Scaling of Deep Chemical Models}, 
DOI={10.26434/chemrxiv-2022-3s512}, journal={ChemRxiv}, publisher={Cambridge Open Engage}, 
author={Frey, Nathan and Soklaski, Ryan and Axelrod, Simon and Samsi, Siddharth and Gomez-Bombarelli, Rafael and Coley, Connor and Gadepally, Vijay}, 
year={2022}} This content is a preprint and has not been peer-reviewed.
```

```
Frey, Nathan, Ryan Soklaski, Simon Axelrod, Siddharth Samsi, Rafael Gomez-Bombarelli, Connor Coley, and Vijay Gadepally. 
"Neural Scaling of Deep Chemical Models." ChemRxiv (2022). Print. This content is a preprint and has not been peer-reviewed.
```
