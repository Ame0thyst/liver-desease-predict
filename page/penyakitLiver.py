import streamlit as st
from PIL import Image

image = Image.open('img/HepatitisC.png')
image2 = Image.open('img/HepatitisB_dewasa.png')
image3 = Image.open('img/HepatitisB_balita.png')



def show_inform_liver():

    st.markdown('''
    <header>
        <h1 style='text-align: center;'>Penyakit Liver / Hepatitis</h1>
    </header>
    <section>
        <h3>Apa itu penyakit hepatitis? </h3>
        <p style='text-align: justify;'>Penyakit Hepatitis
Hepatitis adalah peradangan pada organ hati yang disebabkan oleh infeksi virus, konsumsi alkohol berlebihan, atau penyakit autoimun. Terdapat beberapa jenis virus hepatitis, yaitu A, B, C, D, dan E. Hepatitis B dan C adalah yang paling umum dan dapat menyebabkan penyakit hati kronis</p>
    </section>
''', unsafe_allow_html=True)
   

    st.markdown('''
     <p style="text-align: justify;">Berdasarkan data dari World Health Organization (WHO), diperkirakan 325 juta orang di seluruh dunia hidup dengan infeksi hepatitis B atau C kronis. Indonesia termasuk dalam negara dengan prevalensi hepatitis B yang tinggi, yaitu lebih dari 8% populasi terinfeksi. Hal ini menunjukkan pentingnya meningkatkan kesadaran masyarakat tentang penyakit ini dan upaya pencegahannya</p>
    ''', unsafe_allow_html=True)

    st.markdown('''
   <h2>Kasus Liver Dunia</h2>
        <p style="text-align: justify;">Dibawah ini merupakan data yang dirilis oleh <a href="https://cdafound.org/polaris/global-distribution/"> CDA Foundation</a> yang merupakan perusahan non-profit dan bergerak dalam pemantauan kasus terkait penyakit menular diseluruh dunia.
        </p>
    ''', unsafe_allow_html=True)
        # <p  style="text-align: justify;"><span style="font-weight: bold;"> </span>
        #     </p>
    st.image(image, caption="Gambar 1: Hepatitis C")
    st.image(image2, caption="Gambar 2: Hepatitis B Dewasa")
    st.image(image3, caption="Gambar 3: Hepatitis B Balita")
    st.markdown('''
        <p style="text-align: justify;">Pada <span style=" font-weight: bold;">Gambar 1 </span>Indonesia menempati posisi ke – 6 sebagai negara dengan penderita penyakit liver Hepatitis C terbanyak di dunia dengan total lebih dari satu juta kasus pada tahun 2022. Keadaan yang lebih buruk dapat terlihat pada <span style=" font-weight: bold;">Gambar 2 dan Gambar 3 </span>dimana menunjukkan bahwa total infeksi penyakit liver Hepatitis B ( dewasa ) berjumlah lebih dari 15 juta kasus yang membuat Indonesia menempati peringkat ke -3 sebagai negara dengan kasus Hepatitis B ( dewasa ) terbanyak di dunia pada tahun 2022, dan menempati peringkat ke- 2 sebagai negara dengan penderita Hepatitis B ( Balita ) dengan total lebih dari 600 ribu kasus pada tahun 2022.</p> 
    ''', unsafe_allow_html=True)

    st.markdown('''
    <section>
        <h3>Apa saja sih gejala penyakit hepatitis? </h3>
        <p style='text-align: justify;'Gejala hepatitis dapat bervariasi, namun yang paling umum meliputi:</p>
        </section>
''', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

with col1:
    st.write("""
    - Kelelahan
    - Mual dan muntah
    - Nyeri perut
    - Urin berwarna gelap
    """)

with col2:
    st.write("""
    - Feses berwarna pucat
    - Kulit dan mata kuning (jaundice)
    - Demam
    - Nyeri sendi
    """)

    # st.image(image4)

    # st.markdown('''
    #      <p style="text-align: justify;"><span style="font-weight: bold;"> lorem </span> lorem</p>
    #     <p style="text-align: justify;">lorem:</p>
    #     <ol style="text-align: justify;">
    #         <li>Plorem</li>
            
    #     </ol>
    #     <p style="text-align: justify;">lorem</p>
    # ''', unsafe_allow_html=True)
    # st.image(image5)

    # st.markdown('''
    #      <h2>Kasus Diabetes Melitus di Indonesia</h2>
    #     <p style="text-align: justify;">
    #        lorem
    #     </p>
    #     <p style="text-align: justify;">
    #        lorem
    # ''', unsafe_allow_html=True)

    # st.image(image6)
    # st.markdown('''
    #     <p style="text-align: justify;">
    #         lorem
    #     </p>
    #     <p style="text-align: justify;">
    #         lorem
    #     </p>
    # ''', unsafe_allow_html=True)
    # st.image(image7)
    # st.markdown('''
    #       <h2>Faktor Risiko Diabetes Melitus</h2>
    #     <p style="text-align: justify;">
    #         Slorem
    #     </p>
    #     <p style="text-align: justify;">
    #         lorem</p>
    # ''', unsafe_allow_html=True)
    # st.image(image8)
    # st.markdown('''
    #       <p style="text-align: justify;">
    #                 lorem
    #             </p>
    # ''', unsafe_allow_html=True)
    # st.image(image9)
    # st.markdown('''
    #      <p style="text-align: justify;">
    #                 lorem
    #             </p>
    # ''', unsafe_allow_html=True)
    # st.image(image10)
    # st.markdown('''
    #     <p style="text-align: justify;">
    #                 lorem
    # ''', unsafe_allow_html=True)
    # st.image(image11)
    # st.markdown('''
    #     <p style="text-align: justify;">
    #                lorem
    #             </p>
    # ''', unsafe_allow_html=True)

    # st.markdown('''
    #      <h2>Upaya Pencegahan dan Pengendalian Diaebetes Melitus</h2>
    #     <p style="text-align: justify;">
    #         lorem
    #     </p>
    #     <p style="text-align: justify;">
    #         lorem
    #     </p>
    #     <p style="text-align: justify;">
    #        lorem
    #     </p>
    # ''', unsafe_allow_html=True)
    # st.image(image12)
    # st.markdown('''
    #      <p style="text-align: justify;">
    #        lorem
    #     </p>
    #     <p style="text-align: justify;">
    #         lorem
    #     </p>
    #     <p style="text-align: justify;">
    #        lorem
    #     </p>
    #     <p style="text-align: justify;">
    #         Blorem
    #     </p>
    # ''', unsafe_allow_html=True)
    # st.image(image13)
    # st.markdown('''
    #      <p style="text-align: justify;">
    #         lorem</p>
          
           
    # ''', unsafe_allow_html=True)
   


if __name__ == "__main__":
    show_penyakit_diabetes()
