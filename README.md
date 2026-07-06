# Employee Attrition Prediction using Machine Learning

## Overview

This project predicts whether an employee is likely to leave an organization within the next six months using a supervised Machine Learning model. The goal is to help HR teams identify employees at risk of attrition and enable proactive retention strategies.

The project demonstrates an end-to-end Machine Learning workflow—from synthetic data generation and model training to prediction, containerization, and CI automation.

---

## Problem Statement

Employee attrition is one of the biggest challenges faced by organizations. Early prediction of potential resignations allows HR teams to:

* Improve employee retention
* Reduce recruitment costs
* Plan workforce requirements
* Increase employee satisfaction

This project predicts whether an employee is likely to leave based on workplace and performance-related attributes.

---

## Features

* Synthetic HR dataset generation
* Data preprocessing
* Machine Learning model training
* Employee attrition prediction
* Model serialization using Joblib
* Dockerized application
* GitHub Actions CI pipeline
* Command-line prediction script

---

## Tech Stack

### Programming Language

* Python 3.12

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### DevOps

* Docker
* GitHub Actions

### Version Control

* Git
* GitHub

---

## Project Structure

```text
employee_attrition_ml_model/
│
├── app.py                  # Application entry point
├── train.py                # Train the ML model
├── predict.py              # Predict employee attrition
├── synthetic_data.py       # Generate synthetic HR dataset
├── requirements.txt
├── Dockerfile
│
├── data/
│   └── employees.csv
│
├── models/
│   └── employee_model.pkl
│
└── .github/
    └── workflows/
        └── ml_pipeline.yml
```

---

## Machine Learning Workflow

1. Generate synthetic employee data
2. Preprocess and clean the dataset
3. Train a classification model
4. Evaluate model performance
5. Save the trained model
6. Load the model for predictions
7. Predict employee attrition

---

## Sample Prediction

```text
Prediction: Employee is likely to leave.

Probability of Staying : 36.00%

Probability of Leaving : 64.00%
```

---

## Run Locally

### Clone Repository

```bash
git clone <repository-url>
cd employee_attrition_ml_model
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train.py
```

### Run Prediction

```bash
python predict.py
```

---

## Run with Docker

### Build Docker Image

```bash
docker build -t employee-attrition:v1 .
```

### Run Container

```bash
docker run --rm employee-attrition:v1
```

---

## CI/CD

A GitHub Actions workflow is included to:

* Install dependencies
* Train the Machine Learning model
* Validate predictions
* Verify the project builds successfully

This ensures that every code change is automatically validated before being merged.

---

## Future Enhancements

* Train using real-world HR datasets
* Hyperparameter tuning
* Model explainability using SHAP
* FastAPI deployment
* Kubernetes deployment
* MLflow experiment tracking
* Automated retraining pipeline
* Model monitoring and drift detection

---

## Learning Outcomes

This project helped reinforce practical concepts in:

* Supervised Machine Learning
* Feature engineering
* Model serialization
* Docker containerization
* CI/CD with GitHub Actions
* Production-ready project structure
* End-to-end Machine Learning lifecycle

---

## Author

**Chaitra Thimmaiah**

AI | Machine Learning | Python | Docker | Kubernetes | GitHub Actions | n8n | Agentic AI

Passionate about building production-ready AI systems and intelligent automation solutions.
