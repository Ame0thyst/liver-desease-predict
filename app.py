import streamlit as st
import numpy as np
import pickle

# Memuat model dan scaler menggunakan pickle
with open('liver_model_smote.sav', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Judul Aplikasi
st.title("Liver Disease Prediction")

# Form untuk input pengguna
st.header("Masukkan data pasien:")
age_of_the_patient = st.number_input("Age of the Patient", min_value=1, max_value=100, value=30)
gender_of_the_patient = st.selectbox("Gender of the Patient", ["Male", "Female"])
total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=50.0, value=1.0)
direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=50.0, value=0.1)
alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=1000, value=100)
sgpt_alamine_aminotransferase = st.number_input("SGPT Alamine Aminotransferase", min_value=0, max_value=1000, value=20)
sgot_aspartate_aminotransferase = st.number_input("SGOT Aspartate Aminotransferase", min_value=0, max_value=1000, value=20)
total_protiens = st.number_input("Total Proteins", min_value=0.0, max_value=10.0, value=6.5)
alb_albumin = st.number_input("ALB Albumin", min_value=0.0, max_value=10.0, value=3.0)
a_g_ratio_albumin_and_globulin_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", min_value=0.0, max_value=10.0, value=1.0)

# Konversi gender menjadi nilai numerik
gender_numeric = 1 if gender_of_the_patient == "Male" else 0

# Saat tombol 'Predict' diklik
if st.button("Predict"):
    # Membuat array input dari nilai yang dimasukkan pengguna
    input_data = np.array([[age_of_the_patient, gender_numeric, total_bilirubin, direct_bilirubin, 
                            alkphos_alkaline_phosphotase, sgpt_alamine_aminotransferase, 
                            sgot_aspartate_aminotransferase, total_protiens, alb_albumin, 
                            a_g_ratio_albumin_and_globulin_ratio]])
    
    # Normalisasi input data menggunakan scaler yang sudah disimpan
    input_data_scaled = scaler.transform(input_data)
    
    # Melakukan prediksi
    prediction = model.predict(input_data_scaled)
    
    # Menampilkan hasil prediksi
    if prediction[0] == 1:
        st.success("Pasien terindikasi mengalami penyakit liver.")
    else:
        st.success("Pasien tidak terindikasi mengalami penyakit liver.")
