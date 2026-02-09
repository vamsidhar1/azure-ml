# Azure ML End-to-End MLOps Pipeline

This project demonstrates an end-to-end Machine Learning lifecycle using **Microsoft Azure Machine Learning**, covering training, pipelines, model registry, deployment, and monitoring concepts.

## Project Overview

The goal of this project is to showcase how Azure ML can be used as a platform to manage ML workflows from experimentation to production.

## Architecture Flow

Data → Training → Pipeline Automation → Model Registry → Real-Time Deployment → Monitoring & Retraining

## Key Azure ML Features Used

- Azure ML Jobs
- Azure ML Pipelines
- Model Registry & Versioning
- Managed Online Endpoints
- Blue-Green Deployment Strategy
- Monitoring & Retraining Concepts

## Tech Stack

- Azure Machine Learning
- Python
- Scikit-learn
- Azure ML CLI v2

## Phases Covered

### Phase 1: Data Preparation
- Sample dataset used for training.

### Phase 2: Model Training
- Train a simple ML model using Scikit-learn.
- Log metrics and artifacts.

### Phase 3: Azure ML Job
- Run training as a managed Azure ML job.

### Phase 4: Pipeline Automation
- Convert training job into an Azure ML pipeline.

### Phase 5: Model Registry
- Register and version trained models automatically.

### Phase 6: Model Deployment
- Deploy model as a real-time REST API using Managed Online Endpoints.

### Phase 7: Monitoring & CI/CD
- Monitor endpoint performance.
- Enable retraining using pipelines.
- CI/CD integration using Azure DevOps or GitHub Actions.

## How to Run

```bash
az ml job create --file training/job.yml
az ml job create --file pipeline/pipeline.yml
