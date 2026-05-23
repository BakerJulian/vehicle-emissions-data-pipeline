# Vehicle Emissions Data Pipeline

## Project Overview

This project demonstrates an end-to-end data pipeline using a vehicle emissions dataset. The goal is to take raw CSV data, clean and validate it, prepare it for machine learning, and train a regression model to predict CO2 emissions.

The focus of this project is not only the machine learning model, but also the data preparation steps required before modelling.

## Pipeline Workflow

1. Load raw vehicle emissions data from CSV
2. Inspect columns, data types and missing values
3. Clean duplicate records and invalid target values
4. Save a processed dataset
5. Run data quality checks
6. Build a preprocessing pipeline for numeric and categorical features
7. Train a Random Forest regression model
8. Evaluate the model using MAE, MSE and R2
9. Provide SQL schema and analysis queries

## Tools Used

- Python
- pandas
- scikit-learn
- joblib
- SQL
- Git and GitHub
- VS Code

## Project Structure

```text
vehicle-emissions-data-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── reports/
├── sql/
├── src/
├── requirements.txt
└── README.md