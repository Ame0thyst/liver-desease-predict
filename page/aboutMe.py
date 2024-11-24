# import streamlit as st
# from PIL import Image, ImageDraw, ImageOps

# image = Image.open('img/ikoo.png')

# def show_aboutme():
#     # Deskripsi tentang diri
#     st.markdown('''
#    <h3>Tentang Saya</h3>
#     ''', unsafe_allow_html=True)
    
#     new_image = image.resize((250, 250))
#     st.image(new_image)
#     st.markdown('''
#         <p style="text-align: justify;">
#         Perkenalkan nama saya Gilang Wiko Wicaksono, Saya merupakan Mahasiswa Program Studi  <a style="text-decoration:none" href="https://informatika.umri.ac.id/">Teknik Informatika</a>, <a style="text-decoration:none" href="https://umri.ac.id/"> Universitas Muhammdiyah Riau</a>. Aplikasi ini dibangun untuk tugas akhir skripsi sebagai syarat untuk kelulusan S1 Teknik Informatika. Dibangun menggunakan Algoritma Extreme Gradient Boosting (XGBoost) Sebagai model yang digunakan, lalu model di implementasikan ke framework streamlit untuk membangun aplikasi prediksi penyakit liver
#         </p>
#     ''', unsafe_allow_html=True)

#     #Dosem pembimbing
#     st.markdown('''
#         <h3>Dosen Pembimbing</h3>
#         <ol style="text-align: justify;">
#             <li>Yulia Fatma, S.kom., M.cs</>
#             <li>Fitri Handayani, S.T., M.Kom</li>
#         </ol>
#     ''', unsafe_allow_html=True)

#     # Deskripsi Tujuan 
#     st.markdown(
#     """
#     <h3>Tujuan</h3>
#     <p style="text-align: justify;">
#        Tujuan dari dibangunnya aplikasi ini adalah untuk membantu memprediksi apakah seseorang <span style='color:red'>Terkena Penyakit Liver</span> atau <span style='color:green'>Tidak terkena diabetes</span>. Aplikasi menggunakan model machine learning yang telah dibangun dengan menggunakan algoritma Extreme Gradient Boosting (XGBoost) untuk melakukan prediksi. Selain itu tujuan lainnya adalah untuk melakukan evaluasi kinerja model XGBOOST dalam kasus Prediksi Liver.
        
#     </p>
    
 
#     """,  unsafe_allow_html=True
#     )

import streamlit as st
from PIL import Image

# Memuat gambar
image = Image.open('img/ikoo.png')

def show_aboutme():
    # Deskripsi tentang diri
    st.markdown('''
    <h3>Tentang Saya</h3>
    ''', unsafe_allow_html=True)
    
    # Membuat layout dua kolom
    col1, col2 = st.columns([1, 3])  # Rasio lebar kolom (1:3)

    with col1:
        # Menampilkan gambar
        new_image = image.resize((250, 250))
        st.image(new_image)

    with col2:
        # Menampilkan deskripsi
        st.markdown('''
            <p style="text-align: justify;">
            Perkenalkan nama saya Gilang Wiko Wicaksono, Saya merupakan Mahasiswa Program Studi  
            <a style="text-decoration:none" href="https://informatika.umri.ac.id/">Teknik Informatika</a>, 
            <a style="text-decoration:none" href="https://umri.ac.id/"> Universitas Muhammdiyah Riau</a>. 
            Aplikasi ini dibangun untuk tugas akhir skripsi sebagai syarat untuk kelulusan S1 Teknik Informatika. Dibangun 
            menggunakan Algoritma Extreme Gradient Boosting (XGBoost) Sebagai model yang digunakan, lalu model 
            diimplementasikan ke framework streamlit untuk membangun aplikasi prediksi penyakit liver.
            </p>
        ''', unsafe_allow_html=True)

    # Dosen pembimbing
    st.markdown('''
        <h3>Dosen Pembimbing</h3>
        <ol style="text-align: justify;">
            <li>Yulia Fatma, S.kom., M.cs</li>
            <li>Fitri Handayani, S.T., M.Kom</li>
        </ol>
    ''', unsafe_allow_html=True)

    # Deskripsi Tujuan 
    st.markdown('''
    <h3>Tujuan</h3>
    <p style="text-align: justify;">
       Tujuan dari dibangunnya aplikasi ini adalah untuk membantu memprediksi apakah seseorang 
       <span style='color:red'>Terkena Penyakit Liver</span> atau 
       <span style='color:green'>Tidak terkena diabetes</span>. Aplikasi menggunakan model machine learning yang telah 
       dibangun dengan menggunakan algoritma Extreme Gradient Boosting (XGBoost) untuk melakukan prediksi. Selain itu, 
       tujuan lainnya adalah untuk melakukan evaluasi kinerja model XGBOOST dalam kasus Prediksi Liver.
    </p>
    ''',  unsafe_allow_html=True)
