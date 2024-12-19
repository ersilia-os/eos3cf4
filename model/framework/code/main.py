# imports
import os
import csv
import sys
from molfeat.trans.pretrained.hf_transformers import PretrainedHFTransformer

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    transformer = PretrainedHFTransformer(kind="ChemGPT-4.7M", notation = "selfies")
    features = transformer(smiles_list)
    return features


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["feature{}".format(i) for i in range(128)])  # header
    for o in outputs:
        writer.writerow(o)
