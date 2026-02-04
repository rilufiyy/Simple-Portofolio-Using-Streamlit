import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data", "house_prices_train_clean.csv")
model_dir = os.path.join(base_dir, "models")
model_path = os.path.join(model_dir, "house_price_gwo_log_fe_model.pkl")


def train_and_save_model():
    print(f"loading data from: {data_path}")
    if not os.path.exists(data_path):
        print(f"data file not found: {data_path}")
        return

    df = pd.read_csv(data_path)

    features = [
        "OverallQual", "GrLivArea", "GarageCars", "GarageArea",
        "TotalBsmtSF", "1stFlrSF", "FullBath", "YearBuilt"
    ]
    target = "SalePrice"

    x = df[features]
    y = np.log1p(df[target])

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("model", GradientBoostingRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=4,
            random_state=42
        ))
    ])

    print("training model...")
    pipeline.fit(x, y)

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    joblib.dump(pipeline, model_path)
    print(f"model saved to: {model_path}")


if __name__ == "__main__":
    train_and_save_model()