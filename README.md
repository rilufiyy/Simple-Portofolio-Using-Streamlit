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
<img width="1106" height="802" alt="Screenshot 2026-02-03 225416" src="https://github.com/user-attachments/assets/202691b2-e91f-455c-80d4-35b9dc7402d1" />


## House Price Prediction
<img width="1577" height="947" alt="image" src="https://github.com/user-attachments/assets/8930b082-80ca-49f0-9c53-c5b3cf1eefe3" />

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
<img width="1526" height="760" alt="image" src="https://github.com/user-attachments/assets/4b2d9583-0ce1-400f-9c43-fdc167bb8cb5" />
<img width="1412" height="919" alt="image" src="https://github.com/user-attachments/assets/fa1ecbb8-104e-47d4-a87d-d8f8c89b1b01" />
<img width="1427" height="699" alt="image" src="https://github.com/user-attachments/assets/68476ebf-43ca-4a9c-b9cd-b735a04f5805" />


### Models Compared:
<img width="1379" height="929" alt="image" src="https://github.com/user-attachments/assets/988decd9-8e7b-4ef0-a3d5-646fd536cbab" />
<img width="1367" height="606" alt="image" src="https://github.com/user-attachments/assets/42b757ac-c886-4917-aab2-f73707978e28" />

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
