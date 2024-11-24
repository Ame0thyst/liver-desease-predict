# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from datetime import datetime
# import os


# def liver_prediction_system():
      
#     def save_to_csv(input_data, prediction, filename='new_patient_data.csv'):
#         """
#         Save input data and prediction to CSV file
#         """
#         # Convert input data to dictionary
#         data_dict = {
#             'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'age': input_data[0],
#             'gender': 'Male' if input_data[1] == 1 else 'Female',
#             'total_bilirubin': input_data[2],
#             'direct_bilirubin': input_data[3],
#             'alkphos': input_data[4],
#             'sgpt': input_data[5],
#             'sgot': input_data[6],
#             'total_proteins': input_data[7],
#             'albumin': input_data[8],
#             'ag_ratio': input_data[9],
#             'prediction': prediction
#         }
        
#         # Convert dictionary to DataFrame
#         df_new = pd.DataFrame([data_dict])
        
#         # Check if file exists
#         if os.path.exists(filename):
#             # Append to existing file
#             df_new.to_csv(filename, mode='a', header=False, index=False)
#         else:
#             # Create new file with header
#             df_new.to_csv(filename, index=False)
        
#         return True

#     def show_prediksi_liver():
#         # Load model
#         liver_model = pickle.load(open('ori_70_30_xgboost_model.pkl', 'rb'))

#         # Load scaler
#         scaler = pickle.load(open('scalernew.pkl', 'rb'))

#         # Web title
#         st.markdown("<div class='judul'><h1 style='text-align: center;'>Aplikasi Prediksi Penyakit Liver</h1></div>", unsafe_allow_html=True)

#         # Split columns
#         col1, col2 = st.columns(2)

#         with col1:
#             age_of_the_patient = st.number_input("Age of the Patient", min_value=1, max_value=500, value=30)
#             gender_of_the_patient = st.selectbox("Gender of the Patient", ["Male", "Female"])
#             total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=500.0, value=1.0)
#             direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=500.0, value=0.1)
#             alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=1000, value=100)

#         with col2:
#             sgpt_alamine_aminotransferase = st.number_input("SGPT Alamine Aminotransferase", min_value=0, max_value=1000, value=20)
#             sgot_aspartate_aminotransferase = st.number_input("SGOT Aspartate Aminotransferase", min_value=0, max_value=1000, value=20)
#             total_protiens = st.number_input("Total Proteins", min_value=0.0, max_value=500.0, value=6.5)
#             alb_albumin = st.number_input("ALB Albumin", min_value=0.0, max_value=500.0, value=3.0)
#             a_g_ratio_albumin_and_globulin_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", min_value=0.0, max_value=500.0, value=1.0)   

#         # Map gender to numeric value
#         gender_numeric = 1 if gender_of_the_patient == "Male" else 0

#         # Code for prediction
#         liver_diagnosis = ''

#         # Make prediction button
#         if st.button('Test Prediksi Liver'):
#             # Convert input values to array
#             input_data = [age_of_the_patient, gender_numeric, total_bilirubin, direct_bilirubin, 
#                           alkphos_alkaline_phosphotase, sgpt_alamine_aminotransferase, 
#                           sgot_aspartate_aminotransferase, total_protiens, alb_albumin, 
#                           a_g_ratio_albumin_and_globulin_ratio]
#             # Convert input data to float
#             input_data = np.array(input_data, dtype=float)
#             # Reshape input data to 2D array
#             input_data = input_data.reshape(1, -1)
#             # Normalize input data using the saved scaler object
#             input_data_scaled = scaler.transform(input_data)
#             # Perform prediction
#             liver_prediction = liver_model.predict(input_data_scaled)

#             if liver_prediction[0] == 1:
#                 liver_diagnosis = 'Pasien terindikasi penyakit liver'


#             else:
#                 liver_diagnosis = 'Pasien tidak terkena penyakit liver'
                
#             # Save the data
#             if save_to_csv(input_data[0], liver_prediction[0]):
#                 st.success(liver_diagnosis)
#                 st.info("Data telah disimpan 🐥 terimakasih telah menggunakan layanan ini ")
#             else:
#                 st.success(liver_diagnosis)
#                 st.error("Gagal menyimpan data")

#         # Add a section to display collected data
#         if st.checkbox("Tampilkan Data yang Terkumpul"):
#             if os.path.exists('new_patient_data.csv'):
#                 collected_data = pd.read_csv('new_patient_data.csv')
#                 st.write("### Data yang Telah Terkumpul")
#                 st.dataframe(collected_data)
                
#                 # Add basic statistics
#                 st.write("### Statistik Data")
#                 st.write(f"Total data terkumpul: {len(collected_data)}")
#                 st.write(f"Jumlah kasus positif: {len(collected_data[collected_data['prediction'] == 1])}")
#                 st.write(f"Jumlah kasus negatif: {len(collected_data[collected_data['prediction'] == 0])}")
#             else:
#                 st.info("Belum ada data yang terkumpul")

#     # Menjalankan fungsi show_prediksi_liver
#     show_prediksi_liver()

# if __name__ == "__main__":
#     liver_prediction_system()


import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
import os

def liver_prediction_system():
    def save_to_csv(input_data, prediction, filename='new_patient_data.csv'):
        """
        Save input data and prediction to CSV file
        """
        # Convert input data to dictionary
        data_dict = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'age': input_data[0],
            'gender': 'Male' if input_data[1] == 1 else 'Female',
            'total_bilirubin': input_data[2],
            'direct_bilirubin': input_data[3],
            'alkphos': input_data[4],
            'sgpt': input_data[5],
            'sgot': input_data[6],
            'total_proteins': input_data[7],
            'albumin': input_data[8],
            'ag_ratio': input_data[9],
            'prediction': prediction
        }
        
        # Convert dictionary to DataFrame
        df_new = pd.DataFrame([data_dict])
        
        # Check if file exists
        if os.path.exists(filename):
            # Append to existing file
            df_new.to_csv(filename, mode='a', header=False, index=False)
        else:
            # Create new file with header
            df_new.to_csv(filename, index=False)
        
        return True

    def show_prediksi_liver():
        # Load model
        liver_model = pickle.load(open('ori_70_30_xgboost_model.pkl', 'rb'))

        # Load scaler
        scaler = pickle.load(open('scalernew.pkl', 'rb'))

        # Web title
        st.markdown("<div class='judul'><h1 style='text-align: center;'>Aplikasi Prediksi Penyakit Liver</h1></div>", unsafe_allow_html=True)

        # Split columns
        col1, col2 = st.columns(2)

        with col1:
            age_of_the_patient = st.number_input("Age of the Patient", min_value=1, max_value=500, value=30)
            gender_of_the_patient = st.selectbox("Gender of the Patient", ["Male", "Female"])
            total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=500.0, value=1.0)
            direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=500.0, value=0.1)
            alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=1000, value=100)

        with col2:
            sgpt_alamine_aminotransferase = st.number_input("SGPT Alamine Aminotransferase", min_value=0, max_value=1000, value=20)
            sgot_aspartate_aminotransferase = st.number_input("SGOT Aspartate Aminotransferase", min_value=0, max_value=1000, value=20)
            total_protiens = st.number_input("Total Proteins", min_value=0.0, max_value=500.0, value=6.5)
            alb_albumin = st.number_input("ALB Albumin", min_value=0.0, max_value=500.0, value=3.0)
            a_g_ratio_albumin_and_globulin_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", min_value=0.0, max_value=500.0, value=1.0)   

        # Map gender to numeric value
        gender_numeric = 1 if gender_of_the_patient == "Male" else 0

        # Code for prediction
        liver_diagnosis = ''

        # Make prediction button
        if st.button('Test Prediksi Liver'):
            # Convert input values to array
            input_data = [age_of_the_patient, gender_numeric, total_bilirubin, direct_bilirubin, 
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
            liver_prediction = liver_model.predict(input_data_scaled)

            if liver_prediction[0] == 1:
                liver_diagnosis = 'Pasien terindikasi penyakit liver'
                st.warning(liver_diagnosis)  # Menggunakan warning untuk notifikasi kuning
            else:
                liver_diagnosis = 'Pasien tidak terkena penyakit liver'
                st.success(liver_diagnosis)
                
            # Save the data
            if save_to_csv(input_data[0], liver_prediction[0]):
                st.info("Data telah disimpan 🐥 terimakasih telah menggunakan layanan ini ")
            else:
                st.error("Gagal menyimpan data")

        # Add a section to display collected data
        if st.checkbox("Tampilkan Data yang Terkumpul"):
            if os.path.exists('new_patient_data.csv'):
                collected_data = pd.read_csv('new_patient_data.csv')
                st.write("### Data yang Telah Terkumpul")
                st.dataframe(collected_data)
                
                # Add basic statistics
                st.write("### Statistik Data")
                st.write(f"Total data terkumpul: {len(collected_data)}")
                st.write(f"Jumlah kasus positif: {len(collected_data[collected_data['prediction'] == 1])}")
                st.write(f"Jumlah kasus negatif: {len(collected_data[collected_data['prediction'] == 0])}")
            else:
                st.info("Belum ada data yang terkumpul")

    # Menjalankan fungsi show_prediksi_liver
    show_prediksi_liver()

if __name__ == "__main__":
    liver_prediction_system()