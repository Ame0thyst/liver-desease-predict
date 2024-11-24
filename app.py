import streamlit as st
from page.aboutMe import show_aboutme
from page.penyakitLiver import show_inform_liver
from page.prediksiLiver import show_prediksi_liver, save_to_csv
from streamlit_option_menu import option_menu
import base64
from PIL import Image



logo_path = "img/umri.png"  # Ganti dengan path logo yang sesuai

with open(logo_path, "rb") as logo_file:
    logo_data = base64.b64encode(logo_file.read()).decode("utf-8")

# Membuat Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Judul menu
        options=["About Me", "Informasi Liver", "Prediksi Penyakit Liver"],  # Pilihan menu
        icons=["person", "info-circle", "activity"],  # Ikon (opsional)
        menu_icon="cast",  # Ikon untuk menu utama (opsional)
        default_index=0,  # Default pilihan menu
    )

# Logika untuk Menampilkan Konten Berdasarkan Pilihan Menu
if selected == "About Me":
    show_aboutme()  # Panggil fungsi dari aboutMe.py
elif selected == "Informasi Liver":
    show_inform_liver()  # Panggil fungsi dari penyakitLiver.py
elif selected == "Prediksi Penyakit Liver":
    show_prediksi_liver()  # Panggil fungsi untuk prediksi
    save_to_csv()  # Simpan data jika ada


# Menampilkan footer dengan logo
st.markdown(
    f"""
    <style>
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #white;
        background-color: #F5F5F5;
    }}
    .footer-logo {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .footer-logo img {{
        width: 50px;
        height: 50px;
        object-fit: contain;
        margin-right: 10px;
    }}
    </style>
    <div class="footer">
        <div class="footer-logo">
            <img src="data:image/png;base64,{logo_data}" alt="Logo">
            © 2023 Novrianda, Universitas Muhammadiyah Riau, Teknik Informatika.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
    
