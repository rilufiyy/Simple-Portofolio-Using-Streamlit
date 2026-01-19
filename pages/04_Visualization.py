import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from utils.model_utils import load_sample_data, load_model


st.header("Data Visualization & Model Performance")

tab1, tab2, tab3 = st.tabs(["Dataset Exploration", "Feature Analysis", "Model Metrics"])

uploaded_file = st.file_uploader("Upload Training Dataset (CSV) for Analysis", type=["csv"])

df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = load_sample_data()
    if not df.empty:
        st.info("using default cleaned dataset")

with tab1:
    if df is not None and not df.empty:
        st.subheader("Dataset Preview")
        st.dataframe(df.head())
        st.write(f"shape: {df.shape[0]} rows, {df.shape[1]} columns")

        st.subheader("Missing Values")
        missing = df.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            st.bar_chart(missing)
        else:
            st.success("no missing values found")


with tab2:
    if df is not None and not df.empty:
        st.subheader("Correlation Heatmap (Top 10)")
        numeric_df = df.select_dtypes(include=["int64", "float64"])

        if "SalePrice" in numeric_df.columns:
            corr = numeric_df.corr()
            top_cols = corr["SalePrice"].abs().sort_values(ascending=False).head(10).index
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(numeric_df[top_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

        st.subheader("Feature Distribution")
        feature = st.selectbox("select feature", numeric_df.columns)
        fig_hist = px.histogram(df, x=feature)
        st.plotly_chart(fig_hist, use_container_width=True)


with tab3:
    st.subheader("Model Performance Comparison")

    if df is None or df.empty:
        st.warning("no data available")
    elif "SalePrice" not in df.columns:
        st.error("SalePrice column not found")
    else:
        features = [
            "OverallQual", "GrLivArea", "GarageCars", "GarageArea",
            "TotalBsmtSF", "1stFlrSF", "FullBath", "YearBuilt"
        ]

        available_features = [f for f in features if f in df.columns]
        x = df[available_features]
        y = df["SalePrice"]

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=42
        )

        metrics_data = []

        gwo_model = load_model()

        if gwo_model is not None:
            try:
                log_pred = gwo_model.predict(x_test)
                y_pred_gwo = np.expm1(log_pred)  

                rmse_gwo = np.sqrt(mean_squared_error(y_test, y_pred_gwo))
                mae_gwo = mean_absolute_error(y_test, y_pred_gwo)
                r2_gwo = r2_score(y_test, y_pred_gwo)

                metrics_data.append({
                    "Model": "GWO Optimized Model",
                    "RMSE": rmse_gwo,
                    "MAE": mae_gwo,
                    "R2 Score": r2_gwo
                })
            except Exception as e:
                st.error(f"error evaluating gwo model: {e}")

        lr = LinearRegression()
        lr.fit(x_train, y_train)
        y_pred_lr = lr.predict(x_test)

        rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
        mae_lr = mean_absolute_error(y_test, y_pred_lr)
        r2_lr = r2_score(y_test, y_pred_lr)

        metrics_data.append({
            "Model": "Baseline (Linear Regression)",
            "RMSE": rmse_lr,
            "MAE": mae_lr,
            "R2 Score": r2_lr
        })

        metrics_df = pd.DataFrame(metrics_data)

        st.markdown("### Performance Metrics on Test Set (20% Split)")
        st.dataframe(metrics_df.style.format({
            "RMSE": "{:.2f}",
            "MAE": "{:.2f}",
            "R2 Score": "{:.4f}"
        }))

        st.subheader("RMSE Comparison (Lower is Better)")
        fig_rmse = px.bar(metrics_df, x="Model", y="RMSE", color="Model", text_auto=".2s")
        st.plotly_chart(fig_rmse, use_container_width=True)

        st.subheader("R² Score Comparison (Higher is Better)")
        fig_r2 = px.bar(metrics_df, x="Model", y="R2 Score", color="Model", text_auto=".3f")
        st.plotly_chart(fig_r2, use_container_width=True)