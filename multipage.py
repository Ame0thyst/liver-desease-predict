import streamlit as st
from main import show_prediksi_liver
from evaluation import show_evaluation

st.set_page_config(
    page_title="Liver Disease Prediction App",
    page_icon="🏥",
    layout="wide"
)

# Create navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Prediction", "Evaluation"])

# Display the selected page
if page == "Prediction":
    show_prediksi_liver()
else:
    show_evaluation()