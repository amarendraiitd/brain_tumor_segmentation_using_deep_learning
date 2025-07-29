
# Post-Treatment Glioma Segmentation using Deep Learning (BraTS 2024)

This repository contains code and documentation for my M.Tech thesis at IIT Delhi on segmenting post-treatment gliomas using U-Net and nnU-Net architectures.

## Repository Structure

- `preprocessing/` – Z-score normalization, patch sampling, one-hot encoding.
- `models/` – Implementations of 2.5D U-Net, 3D U-Net, and nnU-Net configuration.
- `training/` – Training scripts, configs, and early stopping.
- `evaluation/` – Dice score calculation, statistical group analysis, and visualization.
- `results/` – Key plots used in presentation and thesis.
- `thesis/` – Final thesis PDF and presentation slides.

## Dataset
This project uses the **BraTS 2024 post-treatment glioma dataset**.
Due to licensing, raw data is not included. Download it from the [BraTS 2024 page](https://www.synapse.org/#!Synapse:syn33274124).

## Models Compared
- 2.5D U-Net
- 3D U-Net
- nnU-Net v2 (self-configuring)

## Key Results
- Highest mean Dice score achieved: **0.75+**
- Best segmentation performance: nnU-Net v2
- Statistical analysis based on lesion size and intensity

## Installation
```bash
conda create -n glioma_seg python=3.9
conda activate glioma_seg
pip install -r requirements.txt
