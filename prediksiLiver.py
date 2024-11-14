import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

def show_prediksi_liver():
    # Load model
    diabetes_model = pickle.load(open('/data/model/liver_model_smote.sav', 'rb'))

    # Load scaler
    scaler = pickle.load(open('scaler.pkl', 'rb'))

    # Web title
    st.markdown("<div class='judul'><h1 style='text-align: center;'>Aplikasi Prediksi Penyakit Liver</h1></div>", unsafe_allow_html=True)

    # Split columns
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input('Input nilai Pregnancies')
        BloodPressure = st.text_input('Input nilai BloodPressure')
        Insulin = st.text_input('Input nilai Insulin')
        DiabetesPedigreeFunction = st.text_input('Input nilai DiabetesPedigreeFunction')
    with col2:
        Glucose = st.text_input('Input nilai Glucose')
        SkinThickness = st.text_input('Input nilai SkinThickness')
        BMI = st.text_input('Input nilai BMI')
        Age = st.text_input('Input nilai Age')

    # Code for prediction
    diab_diagnosis = ''

    # Make prediction button
    if st.button('Test Prediksi Diabetes'):
        # Convert input values to array
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        # Convert input data to float
        input_data = np.array(input_data, dtype=float)
        # Reshape input data to 2D array
        input_data = input_data.reshape(1, -1)
        # Normalize input data using the saved scaler object
        input_data_scaled = scaler.transform(input_data)
        # Perform prediction
        diab_prediction = diabetes_model.predict(input_data_scaled)

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'
        st.success(diab_diagnosis)


if __name__ == "__main__":
    show_prediksi_diabetes()