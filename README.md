# ChemGPT-4.7

ChemGPT (4.7M params) is a language-based transformer model for generative molecular modeling, which was pretrained on the PubChem10M dataset. Pre-trained ChemGPT models are also robust, self-supervised representation learners that generalize to previously unseen regions of chemical space and enable embedding-based nearest-neighbor search. Here we provide the implementation by DataMol.

This model was incorporated on 2023-04-11.


## Information
### Identifiers
- **Ersilia Identifier:** `eos3cf4`
- **Slug:** `molfeat-chemgpt`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Chemical language model`, `Chemical graph model`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `128`
- **Output Consistency:** `Fixed`
- **Interpretation:** 128 features based on a chemical language model

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_000 | float |  | feature 0 for ChemGPT featuriser |
| dim_001 | float |  | feature 1 for ChemGPT featuriser |
| dim_002 | float |  | feature 2 for ChemGPT featuriser |
| dim_003 | float |  | feature 3 for ChemGPT featuriser |
| dim_004 | float |  | feature 4 for ChemGPT featuriser |
| dim_005 | float |  | feature 5 for ChemGPT featuriser |
| dim_006 | float |  | feature 6 for ChemGPT featuriser |
| dim_007 | float |  | feature 7 for ChemGPT featuriser |
| dim_008 | float |  | feature 8 for ChemGPT featuriser |
| dim_009 | float |  | feature 9 for ChemGPT featuriser |

_10 of 128 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3cf4](https://hub.docker.com/r/ersiliaos/eos3cf4)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3cf4.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3cf4.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `6306`
- **Image Size (Mb):** `6365.86`

**Computational Performance (seconds):**
- 10 inputs: `114.3`
- 100 inputs: `114.68`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://molfeat.datamol.io/featurizers/ChemGPT-4.7M](https://molfeat.datamol.io/featurizers/ChemGPT-4.7M)
- **Publication**: [https://www.nature.com/articles/s42256-023-00740-3](https://www.nature.com/articles/s42256-023-00740-3)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos3cf4
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos3cf4
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
