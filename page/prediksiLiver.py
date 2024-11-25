# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from datetime import datetime
# import os
# from datetime import datetime
# import pytz

# def liver_prediction_system():
#     def save_to_csv(input_data, prediction, filename='new_patient_data.csv'):
#         """
#         Save input data and prediction to CSV file
#         """
#         # Convert input data to dictionary
#         data_dict = {
#             'timestamp': datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d %H:%M:%S"),
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
#             alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=2000, value=100)

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
#                          alkphos_alkaline_phosphotase, sgpt_alamine_aminotransferase, 
#                          sgot_aspartate_aminotransferase, total_protiens, alb_albumin, 
#                          a_g_ratio_albumin_and_globulin_ratio]
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
#                 st.warning(liver_diagnosis)  # Menggunakan warning untuk notifikasi kuning
#             else:
#                 liver_diagnosis = 'Pasien tidak terkena penyakit liver'
#                 st.success(liver_diagnosis)
                
#             # Save the data
#             if save_to_csv(input_data[0], liver_prediction[0]):
#                 st.info("Data telah disimpan 🐥 terimakasih telah menggunakan layanan ini ")
#             else:
#                 st.error("Gagal menyimpan data")

#         # Add a section to display collected data
#         if st.checkbox("Tampilkan Data yang Terkumpul"):
#             if os.path.exists('new_patient_data.csv'):
#                 collected_data = pd.read_csv('new_patient_data.csv')
#                 st.write("### Data yang Telah Terkumpul")
#                 st.dataframe(collected_data)
#                 st.write("### Rekapitulasi Data")
#                 total_data = len(collected_data)
#                 positif_cases = len(collected_data[collected_data['prediction'] == 1])
#                 negatif_cases = len(collected_data[collected_data['prediction'] == 0])

#                 # Buat DataFrame untuk tabel statistik
#                 stats_table = pd.DataFrame({
#                     "Keterangan": ["Total Data", "Jumlah Kasus Positif", "Jumlah Kasus Negatif"],
#                     "Jumlah": [total_data, positif_cases, negatif_cases]
#                 })

#                 # Tampilkan tabel
#                 st.table(stats_table)
#             else:
#                 st.info("Belum ada data yang terkumpul")

#     # Menjalankan fungsi show_prediksi_liver
#     show_prediksi_liver()

# if __name__ == "__main__":
#     liver_prediction_system()


## DIBAWAH INI PREDIKSI PENYAKIT LIVER BESERTA REKOMENDASI RS TERDEKAT BERDASARKAN INPUT ALAMAT ✍️✍️

# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from datetime import datetime
# import os
# from datetime import datetime
# import pytz
# import folium
# from streamlit_folium import folium_static
# import requests
# from geopy.geocoders import Nominatim

# def liver_prediction_system():
#     def save_to_csv(input_data, prediction, filename='new_patient_data.csv'):
#         """
#         Save input data and prediction to CSV file
#         """
#         data_dict = {
#             'timestamp': datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d %H:%M:%S"),
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
        
#         df_new = pd.DataFrame([data_dict])
        
#         if os.path.exists(filename):
#             df_new.to_csv(filename, mode='a', header=False, index=False)
#         else:
#             df_new.to_csv(filename, index=False)
        
#         return True

#     def get_nearby_hospitals(user_location):
#         """
#         Get nearby hospitals using OpenStreetMap data
#         """
#         try:
#             # Using Nominatim to get coordinates from address
#             geolocator = Nominatim(user_agent="liver_prediction_app")
#             location = geolocator.geocode(user_location)
            
#             if location:
#                 # Using Overpass API to get nearby hospitals
#                 overpass_url = "http://overpass-api.de/api/interpreter"
#                 overpass_query = f"""
#                 [out:json];
#                 (
#                   node["amenity"="hospital"](around:5000,{location.latitude},{location.longitude});
#                   way["amenity"="hospital"](around:5000,{location.latitude},{location.longitude});
#                   relation["amenity"="hospital"](around:5000,{location.latitude},{location.longitude});
#                 );
#                 out center;
#                 """
                
#                 response = requests.get(overpass_url, params={'data': overpass_query})
#                 data = response.json()
                
#                 hospitals = []
#                 for element in data['elements']:
#                     if 'tags' in element:
#                         name = element['tags'].get('name', 'Unknown Hospital')
#                         if 'center' in element:
#                             lat = element['center']['lat']
#                             lon = element['center']['lon']
#                         else:
#                             lat = element.get('lat')
#                             lon = element.get('lon')
                        
#                         if lat and lon:
#                             hospitals.append({
#                                 'name': name,
#                                 'latitude': lat,
#                                 'longitude': lon
#                             })
                
#                 return location.latitude, location.longitude, hospitals
#             return None, None, []
#         except Exception as e:
#             st.error(f"Error getting hospital data: {str(e)}")
#             return None, None, []

#     def show_hospital_map(user_lat, user_lon, hospitals):
#         """
#         Display a map with user location and nearby hospitals
#         """
#         m = folium.Map(location=[user_lat, user_lon], zoom_start=13)
        
#         # Add user marker
#         folium.Marker(
#             [user_lat, user_lon],
#             popup="Lokasi Anda",
#             icon=folium.Icon(color='red', icon='info-sign')
#         ).add_to(m)
        
#         # Add hospital markers
#         for hospital in hospitals:
#             folium.Marker(
#                 [hospital['latitude'], hospital['longitude']],
#                 popup=hospital['name'],
#                 icon=folium.Icon(color='green', icon='plus', prefix='fa')
#             ).add_to(m)
        
#         return m

#     def show_prediksi_liver():
#         # Load model
#         liver_model = pickle.load(open('ori_70_30_xgboost_model.pkl', 'rb'))
#         scaler = pickle.load(open('scalernew.pkl', 'rb'))

#         st.markdown("<div class='judul'><h1 style='text-align: center;'>Aplikasi Prediksi Penyakit Liver</h1></div>", unsafe_allow_html=True)

#         col1, col2 = st.columns(2)

#         with col1:
#             age_of_the_patient = st.number_input("Age of the Patient", min_value=1, max_value=500, value=30)
#             gender_of_the_patient = st.selectbox("Gender of the Patient", ["Male", "Female"])
#             total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=500.0, value=1.0)
#             direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=500.0, value=0.1)
#             alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=2000, value=100)

#         with col2:
#             sgpt_alamine_aminotransferase = st.number_input("SGPT Alamine Aminotransferase", min_value=0, max_value=1000, value=20)
#             sgot_aspartate_aminotransferase = st.number_input("SGOT Aspartate Aminotransferase", min_value=0, max_value=1000, value=20)
#             total_protiens = st.number_input("Total Proteins", min_value=0.0, max_value=500.0, value=6.5)
#             alb_albumin = st.number_input("ALB Albumin", min_value=0.0, max_value=500.0, value=3.0)
#             a_g_ratio_albumin_and_globulin_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", min_value=0.0, max_value=500.0, value=1.0)   

#         # User location input
#         user_location = st.text_input("Masukkan alamat Anda untuk mencari rumah sakit terdekat", "")

#         gender_numeric = 1 if gender_of_the_patient == "Male" else 0
#         liver_diagnosis = ''

#         if st.button('Test Prediksi Liver'):
#             input_data = [age_of_the_patient, gender_numeric, total_bilirubin, direct_bilirubin, 
#                          alkphos_alkaline_phosphotase, sgpt_alamine_aminotransferase, 
#                          sgot_aspartate_aminotransferase, total_protiens, alb_albumin, 
#                          a_g_ratio_albumin_and_globulin_ratio]
#             input_data = np.array(input_data, dtype=float)
#             input_data = input_data.reshape(1, -1)
#             input_data_scaled = scaler.transform(input_data)
#             liver_prediction = liver_model.predict(input_data_scaled)

#             if liver_prediction[0] == 1:
#                 liver_diagnosis = 'Pasien terindikasi penyakit liver'
#                 st.warning(liver_diagnosis)
                
#                 # Show hospital recommendation
#                 st.error("""
#                 PERHATIAN: Berdasarkan hasil prediksi, Anda disarankan untuk:
#                 1. Segera melakukan pemeriksaan lebih lanjut ke rumah sakit terdekat
#                 2. Konsultasikan hasil tes ini dengan dokter spesialis
#                 3. Jaga pola makan dan hindari minuman beralkohol
#                 """)
                
#                 # Show nearby hospitals if location is provided
#                 if user_location:
#                     st.info("Mencari rumah sakit terdekat dari lokasi Anda...")
#                     user_lat, user_lon, hospitals = get_nearby_hospitals(user_location)
                    
#                     if user_lat and user_lon and hospitals:
#                         st.success(f"Ditemukan {len(hospitals)} rumah sakit di sekitar lokasi Anda")
                        
#                         # Display the map
#                         st.write("### Peta Rumah Sakit Terdekat")
#                         map_data = show_hospital_map(user_lat, user_lon, hospitals)
#                         folium_static(map_data)
                        
#                         # List nearby hospitals
#                         st.write("### Daftar Rumah Sakit Terdekat:")
#                         for idx, hospital in enumerate(hospitals, 1):
#                             st.write(f"{idx}. {hospital['name']}")
#                             maps_url = f"https://www.google.com/maps/dir/?api=1&origin={user_lat},{user_lon}&destination={hospital['latitude']},{hospital['longitude']}&travelmode=driving"
#                             st.markdown(f"[Lihat rute ke {hospital['name']}]({maps_url})")
#                     else:
#                         st.error("Tidak dapat menemukan rumah sakit di sekitar lokasi Anda. Mohon periksa kembali alamat yang dimasukkan.")
                
#             else:
#                 liver_diagnosis = 'Pasien tidak terkena penyakit liver'
#                 st.success(liver_diagnosis)
                
#             if save_to_csv(input_data[0], liver_prediction[0]):
#                 st.info("Data telah disimpan 🐥 terimakasih telah menggunakan layanan ini")
#             else:
#                 st.error("Gagal menyimpan data")

#         # Display collected data section
#         if st.checkbox("Tampilkan Data yang Terkumpul"):
#             if os.path.exists('new_patient_data.csv'):
#                 collected_data = pd.read_csv('new_patient_data.csv')
#                 st.write("### Data yang Telah Terkumpul")
#                 st.dataframe(collected_data)
#                 st.write("### Rekapitulasi Data")
#                 total_data = len(collected_data)
#                 positif_cases = len(collected_data[collected_data['prediction'] == 1])
#                 negatif_cases = len(collected_data[collected_data['prediction'] == 0])

#                 stats_table = pd.DataFrame({
#                     "Keterangan": ["Total Data", "Jumlah Kasus Positif", "Jumlah Kasus Negatif"],
#                     "Jumlah": [total_data, positif_cases, negatif_cases]
#                 })

#                 st.table(stats_table)
#             else:
#                 st.info("Belum ada data yang terkumpul")

#     show_prediksi_liver()

# if __name__ == "__main__":
#     liver_prediction_system()


###DIBAWAH INI SCIPR SUDAH WORK DENGAN ALAMAT DAPAT DIPILIH MANUAL ATAU OTOMATIS

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
import os
import pytz
import folium
from streamlit_folium import folium_static
import requests
from geopy.geocoders import Nominatim

def liver_prediction_system():
    def save_to_csv(input_data, prediction, filename='new_patient_data.csv'):
        """
        Save input data and prediction to CSV file
        """
        data_dict = {
            'timestamp': datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d %H:%M:%S"),
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
        
        df_new = pd.DataFrame([data_dict])
        
        if os.path.exists(filename):
            df_new.to_csv(filename, mode='a', header=False, index=False)
        else:
            df_new.to_csv(filename, index=False)
        
        return True

    def get_location_from_address(address):
        """
        Get coordinates from address using Nominatim
        """
        try:
            geolocator = Nominatim(user_agent="liver_prediction_app")
            location = geolocator.geocode(address)
            if location:
                return location.latitude, location.longitude
            return None, None
        except Exception as e:
            st.error(f"Error getting coordinates: {str(e)}")
            return None, None

    def get_nearby_hospitals(lat, lon):
        """
        Get nearby hospitals using OpenStreetMap data
        """
        try:
            # Using Overpass API to get nearby hospitals
            overpass_url = "http://overpass-api.de/api/interpreter"
            overpass_query = f"""
            [out:json];
            (
              node["amenity"="hospital"](around:5000,{lat},{lon});
              way["amenity"="hospital"](around:5000,{lat},{lon});
              relation["amenity"="hospital"](around:5000,{lat},{lon});
            );
            out center;
            """
            
            response = requests.get(overpass_url, params={'data': overpass_query})
            data = response.json()
            
            hospitals = []
            for element in data['elements']:
                if 'tags' in element:
                    name = element['tags'].get('name', 'Unknown Hospital')
                    if 'center' in element:
                        lat = element['center']['lat']
                        lon = element['center']['lon']
                    else:
                        lat = element.get('lat')
                        lon = element.get('lon')
                    
                    if lat and lon:
                        hospitals.append({
                            'name': name,
                            'latitude': lat,
                            'longitude': lon
                        })
            
            return hospitals
        except Exception as e:
            st.error(f"Error getting hospital data: {str(e)}")
            return []

    def show_hospital_map(user_lat, user_lon, hospitals):
        """
        Display a map with user location and nearby hospitals
        """
        m = folium.Map(location=[user_lat, user_lon], zoom_start=13)
        
        # Add user marker
        folium.Marker(
            [user_lat, user_lon],
            popup="Lokasi Anda",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        
        # Add hospital markers
        for hospital in hospitals:
            folium.Marker(
                [hospital['latitude'], hospital['longitude']],
                popup=hospital['name'],
                icon=folium.Icon(color='green', icon='plus', prefix='fa')
            ).add_to(m)
            
            # Add a line connecting user location to hospital
            folium.PolyLine(
                locations=[[user_lat, user_lon], [hospital['latitude'], hospital['longitude']]],
                weight=2,
                color='blue',
                opacity=0.8
            ).add_to(m)
        
        return m

    def show_prediksi_liver():
        # Load model
        liver_model = pickle.load(open('ori_70_30_xgboost_model.pkl', 'rb'))
        scaler = pickle.load(open('scalernew.pkl', 'rb'))

        st.markdown("<div class='judul'><h1 style='text-align: center;'>Aplikasi Prediksi Penyakit Liver</h1></div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            age_of_the_patient = st.number_input("Age of the Patient", min_value=1, max_value=500, value=30)
            gender_of_the_patient = st.selectbox("Gender of the Patient", ["Male", "Female"])
            total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=500.0, value=1.0)
            direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=500.0, value=0.1)
            alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=2000, value=100)

        with col2:
            sgpt_alamine_aminotransferase = st.number_input("SGPT Alamine Aminotransferase", min_value=0, max_value=1000, value=20)
            sgot_aspartate_aminotransferase = st.number_input("SGOT Aspartate Aminotransferase", min_value=0, max_value=1000, value=20)
            total_protiens = st.number_input("Total Proteins", min_value=0.0, max_value=500.0, value=6.5)
            alb_albumin = st.number_input("ALB Albumin", min_value=0.0, max_value=500.0, value=3.0)
            a_g_ratio_albumin_and_globulin_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", min_value=0.0, max_value=500.0, value=1.0)   

        # Location input with dropdown for common cities
        location_method = st.radio(
            "Pilih metode input lokasi:",
            ["Pilih Kota", "Input Alamat Manual"]
        )

        if location_method == "Pilih Kota":
            # Daftar kota-kota besar di Indonesia
            cities = {
                "Jakarta": "Jakarta, Indonesia",
                "Surabaya": "Surabaya, Jawa Timur, Indonesia",
                "Bandung": "Bandung, Jawa Barat, Indonesia",
                "Medan": "Medan, Sumatera Utara, Indonesia",
                "Semarang": "Semarang, Jawa Tengah, Indonesia",
                "Yogyakarta": "Yogyakarta, Indonesia",
                "Malang": "Malang, Jawa Timur, Indonesia",
                "Denpasar": "Denpasar, Bali, Indonesia",
                "Pekanbaru": "Pekanbaru, Riau, Indonesia"
            }
            selected_city = st.selectbox("Pilih kota terdekat:", list(cities.keys()))
            if selected_city:
                st.session_state['address'] = cities[selected_city]
        else:
            st.session_state['address'] = st.text_input(
                "Masukkan alamat lengkap:",
                help="Contoh: Jalan Sudirman No.1, Jakarta"
            )

        gender_numeric = 1 if gender_of_the_patient == "Male" else 0
        liver_diagnosis = ''

        if st.button('Test Prediksi Liver'):
            input_data = [age_of_the_patient, gender_numeric, total_bilirubin, direct_bilirubin, 
                         alkphos_alkaline_phosphotase, sgpt_alamine_aminotransferase, 
                         sgot_aspartate_aminotransferase, total_protiens, alb_albumin, 
                         a_g_ratio_albumin_and_globulin_ratio]
            input_data = np.array(input_data, dtype=float)
            input_data = input_data.reshape(1, -1)
            input_data_scaled = scaler.transform(input_data)
            liver_prediction = liver_model.predict(input_data_scaled)

            if liver_prediction[0] == 1:
                liver_diagnosis = '🚨 Pasien terindikasi penyakit liver'
                st.warning(liver_diagnosis)
                
                # Show hospital recommendation
                st.error("""
                📌PERHATIAN: Berdasarkan hasil prediksi, Anda disarankan untuk:
                1. Segera melakukan pemeriksaan lebih lanjut ke rumah sakit terdekat
                2. Konsultasikan hasil tes ini dengan dokter spesialis
                3. Jaga pola makan dan hindari minuman beralkohol
                """)
                
                # Get location and show nearby hospitals
                if 'address' in st.session_state and st.session_state['address']:
                    st.info("🔎 Mencari rumah sakit terdekat dari lokasi Anda...")
                    lat, lon = get_location_from_address(st.session_state['address'])
                    
                    if lat and lon:
                        hospitals = get_nearby_hospitals(lat, lon)
                        
                        if hospitals:
                            st.success(f"💡 Ditemukan {len(hospitals)} rumah sakit di sekitar lokasi Anda")
                            
                            # Display the map
                            st.write("### Peta Rumah Sakit Terdekat")
                            map_data = show_hospital_map(lat, lon, hospitals)
                            folium_static(map_data)
                            
                            # List nearby hospitals
                            st.write("### Daftar Rumah Sakit Terdekat:")
                            hospitals_to_show = hospitals[:10]  ## 10 rumah sakit aja cukup kali ya
                            
                            for idx, hospital in enumerate(hospitals_to_show, 1):
                                st.write(f"{idx}. {hospital['name']}")
                                maps_url = f"https://www.google.com/maps/dir/?api=1&origin={lat},{lon}&destination={hospital['latitude']},{hospital['longitude']}&travelmode=driving"
                                st.markdown(f"[Lihat rute ke {hospital['name']}]({maps_url})")
                        else:
                            st.error("Tidak dapat menemukan rumah sakit di sekitar lokasi Anda.")
                    else:
                        st.error("Tidak dapat menemukan koordinat lokasi. Mohon periksa kembali alamat yang dimasukkan.")
                else:
                    st.warning("Silakan masukkan lokasi Anda untuk melihat rumah sakit terdekat.")
                
            else:
                liver_diagnosis = 'Pasien tidak terkena penyakit liver'
                st.success(liver_diagnosis)
                
            if save_to_csv(input_data[0], liver_prediction[0]):
                st.info("Data telah disimpan 🐥 terimakasih telah menggunakan layanan ini")
            else:
                st.error("Gagal menyimpan data")

        # Display collected data section
        if st.checkbox("Tampilkan Data yang Terkumpul"):
            if os.path.exists('new_patient_data.csv'):
                collected_data = pd.read_csv('new_patient_data.csv')
                st.write("### Data yang Telah Terkumpul")
                st.dataframe(collected_data)
                st.write("### Rekapitulasi Data")
                total_data = len(collected_data)
                positif_cases = len(collected_data[collected_data['prediction'] == 1])
                negatif_cases = len(collected_data[collected_data['prediction'] == 0])

                stats_table = pd.DataFrame({
                    "Keterangan": ["Total Data", "Jumlah Kasus Positif", "Jumlah Kasus Negatif"],
                    "Jumlah": [total_data, positif_cases, negatif_cases]
                })

                st.table(stats_table)
            else:
                st.info("Belum ada data yang terkumpul")

    show_prediksi_liver()

if __name__ == "__main__":
    liver_prediction_system()



