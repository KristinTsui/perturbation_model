# Finetuning scGPT for perturbation prediction on T cell data

This repository is built upon **scGPT:Towards Building a Foundation Model for Single-Cell Mutli-omics Using Generative AI**.

## Project Highlights
- Fine-tuned scGPT Model: Leveraging the scGPT architecture to understand and predict perturbation effects in T cell datasets.
- Model is first finetuned using a patient T cell dataset on cell annotation task, then finetuned on perturbation, using the provided adamson dataset.

## Getting Started
```
# clone this repo
git clone https://github.com/KristinTsui/perturbation_model.git
## Install dependencies
mamba env create -f scGPT_env.yaml
```
## Using the finetuned model
Download the finetuned model from https://drive.google.com/drive/u/0/folders/1w1VUHZncB3rEpgUoyTZb-trfDLyjA0_s into the finetuned_model directory.

Load the finetuned model to further finetune using Preturbation_Prediction.ipynb