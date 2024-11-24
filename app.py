import streamlit as st
from page.aboutMe import show_aboutme
from page.penyakitLiver import show_penyakit_diabetes
from page.prediksiLiver import show_prediksi_liver, save_to_csv
from PIL import Image
import base64
from streamlit_option_menu import option_menu

# Mendefinisikan path logo
logo_path = "img/umri.png"  # Ganti dengan path logo yang sesuai

# Membaca logo sebagai base64
with open(logo_path, "rb") as logo_file:
    logo_data = base64.b64encode(logo_file.read()).decode("utf-8")

# Main menu
with st.sidebar:
    selected = option_menu('Main Menu',
    ['Penyakit Liver', 'Prediksi Liver', 'Aboutme'],
    default_index=0)

if selected == "Penyakit Diabetes":
    show_penyakit_diabetes()
elif selected == "Prediksi Diabetes":
    show_prediksi_liver(), save_to_csv()
elif selected == "Aboutme":
    show_aboutme()

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
    
