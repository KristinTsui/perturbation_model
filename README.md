# Finetuning scGPT for perturbation prediction on T cell data

This repository is built upon **scGPT:Towards Building a Foundation Model for Single-Cell Mutli-omics Using Generative AI**.

## Project Highlights
- Fine-tuned scGPT Model: Leveraging the scGPT architecture to understand and predict perturbation effects in T cell datasets.
- Model is first finetuned using a patient T cell dataset on cell annotation task, then finetuned on perturbation, using the provided adamson dataset.

# Clone this repository
```
git clone https://github.com/your-username/T-scGPT
cd T-scGPT
```

# Install dependencies
```
mamba env create -f scGPT.yaml
```
# Example usage

