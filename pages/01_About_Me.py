import streamlit as st

st.header(" About Me")

# Personal Info
st.markdown("""
### **Sri Lutfiya Dwiyeni**
*Mathematics Graduate | Machine Learning Engineer*
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader(" Education & Background")
    st.markdown("""
    - **Degree**: Bachelor of Mathematics
    - **Focus**: Applied Mathematics, Machine Learning, Data Science
    - **Internship**: Data Analyst Intern at **BPS (Badan Pusat Statistik)**
    """)

with col2:
    st.subheader(" Skills & Tech Stack")
    st.markdown("""
    - **Languages**: Python, SQL, R
    - **ML & DL**: TensorFlow, Keras, Scikit-Learn, PyTorch, XGBoost
    - **Web & Dashboard**: Streamlit, Flask
    - **Data Viz**: Matplotlib, Seaborn, Plotly, Tableau
    - **MLOps**: MLflow, Docker, Git
    - **Algorithms**: CNN, LSTM, GRU, Decision Trees, Grey Wolf Optimizer (GWO)
    """)

st.divider()

st.subheader(" Professional Summary")
st.write("""
As a dedicated Machine Learning Engineer, I have strong expertise in developing predictive models 
and optimizing algorithms. My portfolio includes deploying deep learning models for computer vision 
(PlantPal) and optimizing time-series forecasting models using meta-heuristic algorithms like 
Grey Wolf Optimizer. I am proficient in the end-to-end data science lifecycle, from data cleaning 
and visualization to model deployment and monitoring.
""")
