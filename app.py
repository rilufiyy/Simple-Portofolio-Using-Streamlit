import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Sri Lutfiya's Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border-radius: 8px;
    }
    .stSidebar {
        background-color: #2c3e50;
    }
    /* Custom Styling for Sidebar Navigation */
    [data-testid="stSidebarNav"] li div a {
        background-color: #34495e;
        color: white;
        border-radius: 5px;
        margin-bottom: 5px;
        padding: 10px;
        transition: 0.3s;
    }
    [data-testid="stSidebarNav"] li div a:hover {
        background-color: #1abc9c;
        padding-left: 15px;
    }
    /* Styling for the active page if possible */
    [data-testid="stSidebarNav"] [aria-current="page"] {
        background-color: #16a085 !important;
        border-left: 5px solid #f1c40f;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Landing Page Content
st.title("Welcome to My AI/ML Portfolio!")
st.markdown("### Holaa! I'm **Sri Lutfiya Dwiyeni** ")
st.markdown("**AI Machine Learning Engineer | Data Scientist**")

col1, col2 = st.columns([1, 2])

with col1:
    import os
    if os.path.exists("assets/fiya_image.png"):
        st.image("assets/fiya_image.png", caption="Sri Lutfiya Dwiyeni", width=250)
    else:
        st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=SriLutfiya", width=250)
        st.caption("Add 'fiya_image.png' to 'assets/' folder to change this.")

with col2:
    st.markdown("""
    I am a Mathematics graduate and AI Machine Learning Engineer passionate about building intelligent systems.
    I specialize in Deep Learning, Optimization Algorithms (like Grey Wolf Optimizer), and Data Science.
    
    **Highlights:**
    - **PlantPal**: CNN-based Plant Disease Detection
    - **Stock Prediction**: LSTM & GRU models
    - **Optimization**: GWO integrated with LSTM & Decision Trees
    - **Data Science**: Experience as a Data Analyst Intern at BPS
    
    Explore my work using the sidebar!
    """)

st.divider()

# Navigation Hint
st.info("[ALERT!] Use the **Sidebar** to navigate between **About Me**, **Projects**, **Prediction**, and **Visualization** pages.")
