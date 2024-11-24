# import streamlit as st
# from PIL import Image

# # Memuat gambar
# image = Image.open('img/ikoo.png')

# def show_aboutme():
#     # Deskripsi tentang diri
#     st.markdown('''
#     <h3>Tentang Saya</h3>
#     ''', unsafe_allow_html=True)
    
#     # Membuat layout dua kolom
#     col1, col2 = st.columns([1, 3])  # Rasio lebar kolom (1:3)

#     with col1:
#         # Menampilkan gambar
#         new_image = image.resize((250, 250))
#         st.image(new_image)

#     with col2:
#         # Menampilkan deskripsi
#         st.markdown('''
#             <p style="text-align: justify;">
#             Perkenalkan nama saya Gilang Wiko Wicaksono, Saya merupakan Mahasiswa Program Studi  
#             <a style="text-decoration:none" href="https://informatika.umri.ac.id/">Teknik Informatika</a>, 
#             <a style="text-decoration:none" href="https://umri.ac.id/"> Universitas Muhammdiyah Riau</a>. 
#             Aplikasi ini dibangun untuk tugas akhir skripsi sebagai syarat untuk kelulusan S1 Teknik Informatika. Dibangun 
#             menggunakan Algoritma Extreme Gradient Boosting (XGBoost) Sebagai model yang digunakan, lalu model 
#             diimplementasikan ke framework streamlit untuk membangun aplikasi prediksi penyakit liver.
#             </p>
#         ''', unsafe_allow_html=True)

#     # Dosen pembimbing
#     st.markdown('''
#         <h3>Dosen Pembimbing</h3>
#         <ol style="text-align: justify;">
#             <li>Yulia Fatma, S.kom., M.cs</li>
#             <li>Fitri Handayani, S.T., M.Kom</li>
#         </ol>
#     ''', unsafe_allow_html=True)

#     # Deskripsi Tujuan 
#     st.markdown('''
#     <h3>Tujuan</h3>
#     <p style="text-align: justify;">
#        Tujuan dari dibangunnya aplikasi ini adalah untuk membantu memprediksi apakah seseorang 
#        <span style='color:red'>Terkena Penyakit Liver</span> atau 
#        <span style='color:green'>Tidak terkena diabetes</span>. Aplikasi menggunakan model machine learning yang telah 
#        dibangun dengan menggunakan algoritma Extreme Gradient Boosting (XGBoost) untuk melakukan prediksi. Selain itu, 
#        tujuan lainnya adalah untuk melakukan evaluasi kinerja model XGBOOST dalam kasus Prediksi Liver.
#     </p>
#     ''',  unsafe_allow_html=True)


import streamlit as st
from PIL import Image, ImageDraw, ImageOps  

# Fungsi untuk membuat gambar berbentuk lingkaran
def make_circle(image):
    size = (min(image.size),) * 2
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output = ImageOps.fit(image, size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output

# Memuat gambar dosen
image_yulia = Image.open('img/DOSBING1.png')  # Gambar Yulia Fatma
image_fitri = Image.open('img/DOSBING2.jpg')  # Gambar Fitri Handayani
image_ikoo = Image.open('img/ikoo.png')  # Gambar ikoo


# Fungsi utama
def show_aboutme():
    # Deskripsi tentang diri
    st.markdown('''
    <h3>Tentang Saya</h3>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 3])  # Rasio lebar kolom (1:3)
    with col1:
        new_image = image_ikoo.resize((250, 250))
        st.image(new_image)
    with col2:
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
    st.markdown('<h3>Dosen Pembimbing</h3>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)  # Dua kolom untuk pembagian dosen
    with col3:
        # Yulia Fatma
        st.image(make_circle(image_yulia), use_column_width=False, width=150)
        st.markdown('''
        <div style="text-align: center;">
            <p><strong>Yulia Fatma, S.Kom., M.Cs</strong></p>
            <p>NIDN: 123456789</p>
        </div>
        ''', unsafe_allow_html=True)

    with col4:
        # Fitri Handayani
        st.image(make_circle(image_fitri), use_column_width=False, width=150)
        st.markdown('''
        <div style="text-align: center;">
            <p><strong>Fitri Handayani, S.T., M.Kom</strong></p>
            <p>NIDN: 987654321</p>
        </div>
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
    ''', unsafe_allow_html=True)
