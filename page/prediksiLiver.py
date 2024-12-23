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
import xgboost as xgb
import json
from math import radians, sin, cos, sqrt, atan2
##! ayanggg aku skripsian dlu ya :D
##TODO:  AKTIFKAN DEFINISI DIBAWAH INI JIKA INGIN MENAMPILKAN FITUR TO CSV

# def save_to_csv(input_data, prediction, filename='new_patient_data.csv'):
#         """
#         Save input data and prediction to CSV file
#         """
#         data_dict = {
#             'timestamp': datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d %H:%M:%S"),
#             'age': input_data['age_of_the_patient'],
#             'gender': 'Male' if input_data['gender_of_the_patient'] == 1 else 'Female',
#             'total_bilirubin': input_data['total_bilirubin'],
#             'direct_bilirubin': input_data['direct_bilirubin'],
#             'alkphos': input_data['alkphos_alkaline_phosphotase'],
#             'sgpt': input_data['sgpt_alamine_aminotransferase'],
#             'sgot': input_data['sgot_aspartate_aminotransferase'],
#             'total_proteins': input_data['total_protiens'],
#             'albumin': input_data['alb_albumin'],
#             'ag_ratio': input_data['a_g_ratio_albumin_and_globulin_ratio'],
#             'prediction': prediction
#         }
        
#         df_new = pd.DataFrame([data_dict])
        
#         if os.path.exists(filename):
#             df_new.to_csv(filename, mode='a', header=False, index=False)
#         else:
#             df_new.to_csv(filename, index=False)
        
#         return True
##TODO:  INI AKHIR DARI DEFINISI DARI CONVERT INPUT BARU KE CSV
    # Fungsi get_location_from_address tetap sama
def get_location_from_address(address):
        try:
            geolocator = Nominatim(user_agent="liver_prediction_app")
            location = geolocator.geocode(address)
            if location:
                return location.latitude, location.longitude
            return None, None
        except Exception as e:
            st.error(f"Error getting coordinates: {str(e)}")
            return None, None

    # Fungsi get_nearby_hospitals tetap sama
# def get_nearby_hospitals(lat, lon):
        try:
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

    # Fungsi show_hospital_map tetap sama
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points using the Haversine formula
    """
    R = 6371  # Radius of Earth in kilometers

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    
    return distance
def get_nearby_hospitals(lat, lon):
    try:
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
                    hosp_lat = element['center']['lat']
                    hosp_lon = element['center']['lon']
                else:
                    hosp_lat = element.get('lat')
                    hosp_lon = element.get('lon')
                
                if hosp_lat and hosp_lon:
                    # Calculate distance from user location
                    distance = calculate_distance(lat, lon, hosp_lat, hosp_lon)
                    
                    hospitals.append({
                        'name': name,
                        'latitude': hosp_lat,
                        'longitude': hosp_lon,
                        'distance': distance
                    })
        
        # Sort hospitals by distance
        hospitals.sort(key=lambda x: x['distance'])
        
        return hospitals
    except Exception as e:
        st.error(f"Error getting hospital data: {str(e)}")
        return []
    
def show_hospital_map(user_lat, user_lon, hospitals):
    m = folium.Map(location=[user_lat, user_lon], zoom_start=13)
    
    # Add user location marker
    folium.Marker(
        [user_lat, user_lon],
        popup="Lokasi Anda",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    # Add hospital markers with distance information
    for idx, hospital in enumerate(hospitals[:10], 1):  # Only show top 10 closest
        popup_text = f"{idx}. {hospital['name']}<br>Jarak: {hospital['distance']:.2f} km"
        
        folium.Marker(
            [hospital['latitude'], hospital['longitude']],
            popup=popup_text,
            icon=folium.Icon(color='green', icon='plus', prefix='fa')
        ).add_to(m)
        
        # Draw line to hospital
        folium.PolyLine(
            locations=[[user_lat, user_lon], [hospital['latitude'], hospital['longitude']]],
            weight=2,
            color='blue',
            opacity=0.8,
            popup=f"Jarak: {hospital['distance']:.2f} km"
        ).add_to(m)
    
    return m
# def show_hospital_map(user_lat, user_lon, hospitals):
    m = folium.Map(location=[user_lat, user_lon], zoom_start=13)
        
    folium.Marker(
            [user_lat, user_lon],
            popup="Lokasi Anda",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        
    for hospital in hospitals:
            folium.Marker(
                [hospital['latitude'], hospital['longitude']],
                popup=hospital['name'],
                icon=folium.Icon(color='green', icon='plus', prefix='fa')
            ).add_to(m)
            
            folium.PolyLine(
                locations=[[user_lat, user_lon], [hospital['latitude'], hospital['longitude']]],
                weight=2,
                color='blue',
                opacity=0.8
            ).add_to(m)
        
    return m

        

def liver_prediction_system():
        """
        Main function untuk sistem prediksi liver
        """
        # Load model dari JSON
        liver_model = xgb.XGBClassifier()
        liver_model.load_model('xgboost_model_smote.json')
        
        # Load feature names
        with open('feature_names.json', 'r') as f:
            feature_dict = json.load(f)
        feature_names = feature_dict['feature_names']
        
        # Load scaler
        scaler = pickle.load(open('scaler.pkl', 'rb'))

        st.markdown("<div class='judul'><h1 style='text-align: center;'>Aplikasi Prediksi Penyakit Liver</h1></div>", unsafe_allow_html=True)

        # Sisa kode UI dan logika prediksi (semua kode yang ada di show_prediksi_liver)
        col1, col2 = st.columns(2)
        with col1:
                age_of_the_patient = st.number_input("Umur", min_value=1, max_value=500, value=30)
                gender_of_the_patient = st.selectbox("Jenis Kelamin", ["Male", "Female"])
                total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, max_value=500.0, value=1.0)
                direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, max_value=500.0, value=0.1)
                alkphos_alkaline_phosphotase = st.number_input("Alkphos Alkaline Phosphotase", min_value=0, max_value=2000, value=100)

        with col2:
                sgpt_alamine_aminotransferase = st.number_input("SGPT Alamine Aminotransferase", min_value=0, max_value=1000, value=20)
                sgot_aspartate_aminotransferase = st.number_input("SGOT Aspartate Aminotransferase", min_value=0, max_value=1000, value=20)
                total_protiens = st.number_input("Total Proteins", min_value=0.0, max_value=500.0, value=6.5)
                alb_albumin = st.number_input("ALB Albumin", min_value=0.0, max_value=500.0, value=3.0)
                a_g_ratio_albumin_and_globulin_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", min_value=0.0, max_value=500.0, value=1.0)   

            # Location input tetap sama
        location_method = st.radio(
                "Pilih metode input lokasi:",
                ["Pilih Kota", "Input Alamat Manual"]
            )
        if location_method == "Pilih Kota":
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
                # Membuat dictionary input sesuai feature names
                input_dict = {
                    'age_of_the_patient': age_of_the_patient,
                    'gender_of_the_patient': gender_numeric,
                    'total_bilirubin': total_bilirubin,
                    'direct_bilirubin': direct_bilirubin,
                    'alkphos_alkaline_phosphotase': alkphos_alkaline_phosphotase,
                    'sgpt_alamine_aminotransferase': sgpt_alamine_aminotransferase,
                    'sgot_aspartate_aminotransferase': sgot_aspartate_aminotransferase,
                    'total_protiens': total_protiens,
                    'alb_albumin': alb_albumin,
                    'a_g_ratio_albumin_and_globulin_ratio': a_g_ratio_albumin_and_globulin_ratio
                }

                # Konversi ke DataFrame dan urutkan sesuai feature names
                input_df = pd.DataFrame([input_dict])
                input_df = input_df[feature_names]
                
                # Scale input data
                input_data_scaled = scaler.transform(input_df)
                
                # Prediksi
                liver_prediction = liver_model.predict(input_data_scaled)
                prediction_proba = liver_model.predict_proba(input_data_scaled)

                if liver_prediction[0] == 0:
                    liver_diagnosis = '🚨 Pasien terindikasi penyakit liver'
                    st.warning(liver_diagnosis)
                    st.write(f"Probabilitas: {prediction_proba[0][0]:.2%}")
                    
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
                                hospitals_to_show = hospitals[:10]

                                for idx, hospital in enumerate(hospitals_to_show, 1):
                                    st.write(f"{idx}. {hospital['name']} (Jarak: {hospital['distance']:.2f} km)")
                                    maps_url = f"https://www.google.com/maps/dir/?api=1&origin={lat},{lon}&destination={hospital['latitude']},{hospital['longitude']}&travelmode=driving"
                                    st.markdown(f"[Lihat rute ke {hospital['name']}]({maps_url})")
                                
                                # for idx, hospital in enumerate(hospitals_to_show, 1):
                                #     st.write(f"{idx}. {hospital['name']}")
                                #     maps_url = f"https://www.google.com/maps/dir/?api=1&origin={lat},{lon}&destination={hospital['latitude']},{hospital['longitude']}&travelmode=driving"
                                #     st.markdown(f"[Lihat rute ke {hospital['name']}]({maps_url})")
                            else:
                                st.error("Tidak dapat menemukan rumah sakit di sekitar lokasi Anda.")
                        else:
                            st.error("Tidak dapat menemukan koordinat lokasi. Mohon periksa kembali alamat yang dimasukkan.")
                    else:
                        st.warning("Silakan masukkan lokasi Anda untuk melihat rumah sakit terdekat.")
                    
                else:
                    liver_diagnosis = 'Pasien tidak terkena penyakit liver'
                    st.success(liver_diagnosis)
                    st.write(f"Probabilitas: {prediction_proba[0][1]:.2%}")


##? dibawah ini fitur lama tentang data inputan bisa tersave dan di download sebagai csv

        #         if save_to_csv(input_dict, liver_prediction[0]):
        #             st.info("Data telah disimpan 🐥 terimakasih telah menggunakan layanan ini")
        #         else:
        #             st.error("Gagal menyimpan data")

        #     # Display collected data section
        # if st.checkbox("Tampilkan Data yang Terkumpul"):
        #         if os.path.exists('new_patient_data.csv'):
        #             collected_data = pd.read_csv('new_patient_data.csv')
        #             st.write("### Data yang Telah Terkumpul")
        #             st.dataframe(collected_data)
        #             st.write("### Rekapitulasi Data")
        #             total_data = len(collected_data)
        #             positif_cases = len(collected_data[collected_data['prediction'] == 0])
        #             negatif_cases = len(collected_data[collected_data['prediction'] == 1])

        #             stats_table = pd.DataFrame({
        #                 "Keterangan": ["Total Data", "Jumlah Kasus Positif", "Jumlah Kasus Negatif"],
        #                 "Jumlah": [total_data, positif_cases, negatif_cases]
        #             })

        #             st.table(stats_table)
        #         else:
        #             st.info("Belum ada data yang terkumpul")
##? Ini batas akhir fitur koleksi data input dan show data input

if __name__ == "__main__":
    liver_prediction_system()