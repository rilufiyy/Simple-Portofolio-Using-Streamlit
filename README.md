# Simple-Portofolio-Using-Streamlit
This repository contains a machine learning portfolio application built with Streamlit, focusing on house price prediction, model evaluation, and data visualization.
The project is designed as an end-to-end ML portfolio, showcasing:
- Data preprocessing & feature selection
Model rebuilding and persistence
- Interactive prediction
- Model performance comparison
- Clean, multi-page Streamlit application

## Profile (About Me)

The Profile page introduces the author and serves as a personal portfolio section.
It highlights:
- Background in Machine Learning & Data Science
- Previous AI/ML projects
- GitHub profile and technical interests
Implemented in: pages/01_About_Me.py

## Projects Showcase
The Projects page displays selected ML & AI projects with descriptions, tech stacks, and GitHub links.
Highlighted projects include:
- CNN-based Plant Disease Detection
- Clinical Research RAG Mini Chatbot
- Optimization using Grey Wolf Optimizer (GWO)
- Video Captioning with BLIP-2
Implemented in: pages/02_Projects.py

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
.
├── assets/                 # Images & visual assets
├── data/                   # Dataset files
│   ├── house_prices_train_clean.csv
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
│
├── models/
│   └── house_price_gwo_log_fe_model.pkl
│
├── notebook/               # Experimental notebooks
├── pages/                  # Streamlit multi-page app
│   ├── 01_About_Me.py
│   ├── 02_Projects.py
│   ├── 03_Prediction.py
│   └── 04_Visualization.py
│
├── utils/
│   └── model_utils.py
│
├── app.py                  # Streamlit entry point
├── rebuild_model.py        # Model rebuild script
├── requirements.txt
└── README.md
