import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def show_prediksi_liver():
    # Load model
    diabetes_model = pickle.load(open('ori_70_30_xgboost_model.pkl', 'rb'))

    # Load scaler
    scaler = pickle.load(open('scaler.pkl', 'rb'))

    # Web title
    st.markdown("<div class='judul'><h1 style='text-align: center;'>Aplikasi Prediksi Penyakit Liver</h1></div>", unsafe_allow_html=True)

    # Split columns
    col1, col2 = st.columns(2)

    with col1:
        age_of_the_patient = st.number_input("Age of the Patient", min_value=1, max_value=100, value=30)
        gender_of_the_patient = st.selectbox("Gender of the Patient", ["Male", "Female"])
        total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=50.0, value=1.0)
        direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=50.0, value=0.1)
        alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=1000, value=100)
         
    with col2:
        sgpt_alamine_aminotransferase = st.number_input("SGPT Alamine Aminotransferase", min_value=0, max_value=1000, value=20)
        sgot_aspartate_aminotransferase = st.number_input("SGOT Aspartate Aminotransferase", min_value=0, max_value=1000, value=20)
        total_protiens = st.number_input("Total Proteins", min_value=0.0, max_value=10.0, value=6.5)
        alb_albumin = st.number_input("ALB Albumin", min_value=0.0, max_value=10.0, value=3.0)
        a_g_ratio_albumin_and_globulin_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", min_value=0.0, max_value=10.0, value=1.0)   
     
        # Age = st.text_input('Input nilai Age')

    # Code for prediction
    diab_diagnosis = ''

    # Make prediction button
    if st.button('Test Prediksi Liver'):
        # Convert input values to array
        input_data = [age_of_the_patient, gender_of_the_patient, total_bilirubin, direct_bilirubin, 
                            alkphos_alkaline_phosphotase, sgpt_alamine_aminotransferase, 
                            sgot_aspartate_aminotransferase, total_protiens, alb_albumin, 
                            a_g_ratio_albumin_and_globulin_ratio]
        # Convert input data to float
        input_data = np.array(input_data, dtype=float)
        # Reshape input data to 2D array
        input_data = input_data.reshape(1, -1)
        # Normalize input data using the saved scaler object
        input_data_scaled = scaler.transform(input_data)
        # Perform prediction
        diab_prediction = diabetes_model.predict(input_data_scaled)

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terindikasi penyakit liver'
        else:
            diab_diagnosis = 'Pasien tidak terkena penyakit liver'
        st.success(diab_diagnosis)


if __name__ == "__main__":
    show_prediksi_liver()