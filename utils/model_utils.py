import os
import joblib
import pandas as pd
import streamlit as st


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_dir, "models", "house_price_gwo_log_fe_model.pkl")
data_path = os.path.join(base_dir, "data", "house_prices_train_clean.csv")


@st.cache_resource
def load_model(path=model_path):
    if not os.path.exists(path):
        st.error(f"model file not found at: {path}")
        return None

    try:
        model = joblib.load(path)
        return model
    except Exception as e:
        st.error(f"error loading model: {e}")
        return None


def load_sample_data():
    if os.path.exists(data_path):
        try:
            df = pd.read_csv(data_path)
            return df
        except Exception as e:
            st.error(f"error loading data: {e}")
            return pd.DataFrame()
    else:
        st.error(f"data file not found at: {data_path}")
        return pd.DataFrame()


def predict_data(model, input_df):
    try:
        features = [
            "OverallQual", "GrLivArea", "GarageCars", "GarageArea",
            "TotalBsmtSF", "1stFlrSF", "FullBath", "YearBuilt"
        ]

        missing_cols = [col for col in features if col not in input_df.columns]
        if missing_cols:
            st.error(f"missing required columns: {missing_cols}")
            return None

        x = input_df[features].copy()

        preds_log = model.predict(x)
        preds_real = pd.Series(preds_log).apply(lambda v: pow(2.718281828, v) - 1)

        return preds_real

    except Exception as e:
        st.error(f"prediction failed: {e}")
        return None