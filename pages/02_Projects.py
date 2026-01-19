import streamlit as st
import os

st.header(" My Projects")

def show_project(title, description, tech_stack, image_url=None, github_link="#"):
    with st.expander(f" {title}", expanded=True):
        col1, col2 = st.columns([1, 3])
        if image_url:
            with col1:
                st.image(image_url, width=250)   
        with col2:
            st.markdown(f"**Description:** {description}")
            st.markdown(f"**Tech Stack:** `{tech_stack}`")
            st.markdown(f"[ View Code / Demo]({github_link})")

# Project 1
plantpal_img = "assets/plantpal_image.jpg"
if not os.path.exists(plantpal_img):
    plantpal_img = "https://placehold.co/600x400?text=PlantPal"

show_project(
    title="PlantPal - CNN Plant Disease Detection",
    description="A Deep Learning application utilizing Convolutional Neural Networks (CNN) to detect plant diseases from leaf images. The model was deployed to a web interface to assist farmers in early diagnosis.",
    tech_stack="Python, TensorFlow, Streamlit, OpenCV",
    image_url=plantpal_img,
    github_link="https://github.com/PlantPal-C242-PS112/PlantPal-ML"
)

# Project 2
clinical_img = "assets/clinical_RAG.png"
if not os.path.exists(clinical_img):
    clinical_img = "https://placehold.co/600x400?text=Clinical+Research+RAG"

show_project(
    title="Clinical Research RAG Mini Chatbot",
    description="A mini Retrieval-Augmented Generation (RAG) chatbot designed to answer clinical psychology questions.",
    tech_stack="Python, LangChain, OpenAI API, Vector DB, FAISS, Streamlit",
    image_url=clinical_img,
    github_link="https://github.com/rilufiyy/Clinical-Research-RAG-Mini-Chatbot"
)

# Project 3
gwo_img = "assets/Grey-Wolf-Optimizer.jpg"
if not os.path.exists(gwo_img):
    gwo_img = "https://placehold.co/600x400?text=GWO+Optimization"

show_project(
    title="Optimization with Grey Wolf Optimizer (GWO)",
    description="Research-focused project implementing the Grey Wolf Optimizer (GWO).",
    tech_stack="Python, Scikit-Learn, GWO Algorithm, NumPy",
    image_url=gwo_img,
    github_link="https://github.com/rilufiyy/GWO-with-Levy-Flight---Pima-Diabetes"
)

# Project 4
video_img = "assets/realtimediagram.png"
if not os.path.exists(video_img):
    video_img = "https://placehold.co/600x400?text=Video+Captioning"

show_project(
    title="Video Captioning using BLIP 2 Hugging Face Model",
    description="End-to-end video captioning pipeline using BLIP-2 from Hugging Face.",
    tech_stack="Python, LangChain, OpenAI API, Vector DB",
    image_url=video_img,
    github_link="https://github.com/rilufiyy/Video-Captioning-using-BLIP-2-Hugging-Face-Model"
)

st.divider()

st.subheader(" Find me on GitHub")
col1, col2 = st.columns([1, 4])

with col1:
    logo_path = "assets/logo_fiya.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=500)
    else:
        st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=100)

with col2:
    st.markdown("### Check out more of my work!")
    st.markdown("[**github.com/rilufiyy**](https://github.com/rilufiyy)")
    st.button(
        "Go to GitHub Profile",
        on_click=lambda: st.markdown(
            '<meta http-equiv="refresh" content="0;url=https://github.com/rilufiyy">',
            unsafe_allow_html=True
        )
    )