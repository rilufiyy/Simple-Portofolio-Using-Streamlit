import streamlit as st
import pandas as pd
from utils.model_utils import load_model, predict_data, load_sample_data

st.header(" House Price Prediction")

st.markdown("""
Upload your CSV file containing the house features to predict the price.
**Required columns:** The model expects specific features (e.g., `GrLivArea`, `OverallQual`, etc. based on training).
""")

model = load_model()

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        input_df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(input_df.head())

        # Prediction Button
        if st.button("Run Prediction"):
            if model:
                with st.spinner("Running predictions..."):
                    preds = predict_data(model, input_df)
                    
                    if preds is not None:
                        input_df['Predicted_Price'] = preds
                        
                        st.success("Prediction Completed!")
                        st.subheader("Results")
                        st.dataframe(input_df)
                        
                        # Simple chart of predictions
                        st.subheader("Price Distribution of Predictions")
                        st.bar_chart(input_df['Predicted_Price'])
                        
                        # Download results
                        csv = input_df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="Download Predictions as CSV",
                            data=csv,
                            file_name='predictions.csv',
                            mime='text/csv',
                        )
            else:
                st.error("Model is not loaded. Please check the model path.")
                
    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Awaiting CSV file upload. Don't have one? See sample format below.")
    st.write("### Sample Data Format")
    sample_df = load_sample_data()
    st.dataframe(sample_df)
