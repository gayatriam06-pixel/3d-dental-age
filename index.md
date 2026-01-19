# Age Estimation from 3D Dental Casts (STL-based)

## Overview

This project presents a **proof-of-concept machine learning pipeline** for **forensic age and sex estimation** using **3D dental casts in STL format**.  
The model learns global morphological characteristics of the dental arch and predicts:

- **Chronological age** (regression)
- **Biological sex** (classification)

The system is designed for **limited sample size**, **short development time**, and **forensic defensibility**, making it suitable for academic evaluation and viva examinations.

---

## Key Principles

- **Input to the model:**  
  3D dental cast geometry only (STL file)

- **Outputs from the model:**  
  - Estimated age (years)  
  - Estimated sex (Male/Female)

- **Training labels (age & sex):**  
  Extracted **only during training** from standardized STL filenames

- **Inference:**  
  New STL files **do not contain age or sex information** and are treated as unlabeled forensic samples

---

## Dataset Description

- Sample size: **70 STL files**
  - 35 upper jaw
  - 35 lower jaw
- Format: `.stl` (3D surface meshes)
- Source: Dental casts
- Privacy:  
  **Raw STL files are excluded from version control** and remain local

### Filename Convention (Training Only)

<any_prefix><Gender><Age><UpperJaw|LowerJaw>.stl

Example:
```
LH07171055_M42_LowerJaw.stl
```

- Gender: `M` or `F`
- Age: integer (years)
- Files not following this convention are **ignored automatically**

---

## Methodology

### 1. Feature Extraction (Global Morphology)

From each STL file, the following **global 3D features** are extracted:

- Mesh volume
- Surface area
- Mean bounding box dimension
- Number of faces
- Number of vertices

These features capture cumulative age-related dental changes such as wear, flattening, and arch remodeling without requiring tooth-level segmentation.

---

### 2. Model Architecture

Two separate machine learning models are trained:

- **Age Estimation:**  
  Random Forest Regressor

- **Sex Classification:**  
  Random Forest Classifier

This dual-head approach improves interpretability and forensic relevance.

---

### 3. Training vs Inference Separation

| Stage | STL Geometry | Age/Sex Used |
|----|----|----|
| Training | ✅ Yes | ✅ Yes (labels) |
| Feature Extraction | ✅ Yes | ❌ No |
| Inference | ✅ Yes | ❌ No |

This ensures **no label leakage** and maintains forensic validity.

---

## Project Structure

```
Age_Estimation_3D_Dental/
│
├── README.md
├── .gitignore
│
├── data/
│ ├── raw/ # STL files (ignored by git)
│ ├── processed/ # Extracted dataset CSV
│ └── README.md
│
├── src/
│ ├── config.py
│ ├── feature_extraction.py
│ ├── dataset_builder.py
│ ├── train_model.py
│ └── predict.py
│
├── models/ # Trained models (optional to store)
│
├── diagrams/
│ └── workflow.png
│
└── requirements.txt
```

---

## Installation

### Recommended Python Version
- Python **3.10 or 3.11** (python.org distribution)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Usage
Step 1: Place STL files (Training)

Copy all labeled STL files into:
```data/raw/
```

Step 2: Build Dataset
```
python src/dataset_builder.py
```

Output:
```
data/processed/dataset.csv
```

Step 3: Train Models
```
python src/train_model.py
```
Outputs:
```
models/age_model.pkl
models/sex_model.pkl
```

Step 4: Predict from New STL (Inference)

Provide an unlabeled STL file and run:
```
python src/predict.py
```

Example output:
```
Predicted Age (years): 36.4
Predicted Sex: Male
```

Expected Performance (Proof-of-Concept)

Given the limited dataset size:

= Sex classification accuracy: ~75–85%

= Age estimation error: ±5–8 years (MAE)

= These results are intended for academic demonstration, not clinical deployment.

Ethical & Forensic Considerations

- No personal identifiers are stored in the repository

- Raw dental STL files are excluded from version control

- The system avoids manual annotation bias

- The methodology emphasizes reproducibility and transparency


Limitations & Future Work

- Increase dataset size for improved accuracy

- Incorporate curvature-based and wear-specific features

- Extend to deep learning (e.g., PointNet) with larger datasets

- Separate models for upper and lower jaws
