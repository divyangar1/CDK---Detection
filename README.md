# CKD Detection and Severity Prediction

A machine learning-based system for predicting Chronic Kidney Disease (CKD) and estimating its severity using clinical and laboratory parameters.

## Project Overview

Chronic Kidney Disease is a progressive condition that can be difficult to identify in its early stages. This project uses machine learning techniques to analyze patient clinical data and predict the presence and severity of CKD.

The system includes data preprocessing, feature transformation, machine learning model training, model evaluation, and an interactive Streamlit-based prediction interface.

## Objectives

- Predict whether a patient is likely to have CKD.
- Predict the severity/stage of CKD.
- Apply appropriate data preprocessing techniques.
- Compare different machine learning algorithms.
- Evaluate model performance using standard classification metrics.
- Provide an easy-to-use interface for entering patient parameters and obtaining predictions.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## Machine Learning Workflow

1. Dataset Collection
2. Data Preprocessing
3. Handling Missing Values
4. Categorical Feature Encoding
5. Feature Scaling
6. Principal Component Analysis (PCA)
7. Train-Test Split
8. Machine Learning Model Training
9. Model Evaluation
10. CKD Prediction
11. CKD Severity Prediction

## Machine Learning Models

The project evaluates multiple classification algorithms, including:

- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest

Random Forest is used for the final prediction because of its strong classification performance and ability to handle multiple clinical features.

## Model Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC Curve
- AUC

## Project Structure

```text
CKD-Detection/
│
├── app/
│   └── app.py
│
├── datasets/
│   ├── sdcd.csv
│   └── severity_dataset.csv
│
├── models/
│   └── ckd_severity_random_forest.pkl
│
├── notebooks/
│   ├── sdcdk.ipynb
│   └── severity.ipynb
│
├── requirements.txt
└── README.md