# Finetuning scGPT for perturbation prediction on T cell data

This repository is built upon **scGPT:Towards Building a Foundation Model for Single-Cell Mutli-omics Using Generative AI**.

## Project Highlights

- Fine-tuned scGPT Model: Utilizes the scGPT architecture to predict perturbation effects in T cell datasets. The perturbation prediction feature is detailed in features/Perturbation_Prediction.ipynb.

- Foundation Model Fine-tuning: Initially fine-tuned using a patient T cell dataset for cell annotation tasks. The next phase targets further fine-tuning on perturbation prediction, employing the Adamson dataset provided in data/.

## Background
Due to the absence of perturb-seq data from our clinical trial dataset, direct training on the perturb-seq feature is not feasible. To overcome this limitation, the approach involves initially fine-tuning the model on the cell annotation feature, using an available RNA-seq dataset from a GD2 CAR T clinical trial. Following this initial fine-tuning phase, the model will be further refined on the perturbation prediction feature, utilizing the dataset provided in the tutorial. This step-wise fine-tuning strategy is designed to adapt the model for perturbation prediction tasks in the absence of direct perturb-seq training data.

## Getting Started
```shell
# clone this repo
git clone https://github.com/KristinTsui/perturbation_model.git

## Install dependencies
mamba env create -f scGPT_env.yaml
```

## Requirements
- 32 GB RAM
- NVIDIA GPU and CUDA 11.7


## Using the finetuned model
Download the finetuned model from https://drive.google.com/drive/u/0/folders/1w1VUHZncB3rEpgUoyTZb-trfDLyjA0_s into the finetuned_model directory.

Load the finetuned model to further finetune using Preturbation_Prediction.ipynb

Update 22/03/24: Please ignore the DVC files, could not establish connection to my google drive. Please use the provided link to download the finetuned model.

## Design Doc
Current Goals: 
Refine the scGPT model and use the perturbation prediction feature to predict the impact of specific gene knockdown on patient outcomes. Visualize the predictions for the top 20 differentially expressed (DE) genes. 


Non-Goals: 
Aim for prefect predictions from the model. 



