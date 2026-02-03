# Simple-Portofolio-Using-Streamlit
This repository contains a machine learning portfolio application built with Streamlit, focusing on house price prediction, model evaluation, and data visualization.
The project is designed as an end-to-end ML portfolio, showcasing:
- Data preprocessing & feature selection
Model rebuilding and persistence
- Interactive prediction
- Model performance comparison
- Clean, multi-page Streamlit application

<img width="1565" height="583" alt="image" src="https://github.com/user-attachments/assets/b32d6e6a-ef7a-4f31-ad03-316116b49088" />

## Profile (About Me)

<img width="1485" height="657" alt="image" src="https://github.com/user-attachments/assets/bb0f9976-f03d-47c1-9da7-b7509a35510c" />


## Projects Showcase
![Uploading image.png…]()


## House Price Prediction
The Prediction page allows users to:
- Upload a CSV file
- Predict house prices using a trained ML model
- View predicted values directly in the app
### Model Details
- Algorithm: Gradient Boosting Regressor
- Target transformation: log1p(SalePrice)
- Predictions are inverse-transformed using expm1
- Model loaded from a saved .pkl file
Implemented in:
pages/03_Prediction.py
utils/model_utils.py
models/house_price_gwo_log_fe_model.pkl

## Data Visualization & Model Performance
The Visualization page provides interactive analysis and evaluation.
### Features: 
- Dataset preview & shape
- Missing value inspection
- Correlation heatmap (top correlated features)
- Feature distribution plots
- Model perf ormance comparison
### Models Compared:
- Optimized Model (Saved Model)
- Baseline Linear Regression
### Metrics Used:
- RMSE
- MAE
- R² Score
Implemented in: pages/04_Visualization.py

## Features Used for Modeling
The prediction model uses the following features:
OverallQual
GrLivArea
GarageCars
GarageArea
TotalBsmtSF
1stFlrSF
FullBath
YearBuilt

## Repository Structure
<img width="472" height="820" alt="image" src="https://github.com/user-attachments/assets/5e1a583b-64af-4691-8b26-9b9228d714ed" />
