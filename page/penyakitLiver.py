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
        <p style="text-align: justify;">Dibawah ini merupakan data yang dirilis oleh <a href="www"> CDA Foundation</a> yang merupakan perusahan non-profit dan bergerak dalam pemantauan kasus terkait penyakit menular diseluruh dunia.
        </p>
        <p  style="text-align: justify;"><span style="font-weight: bold;">lorem. </span>lorem
            .</p>
    ''', unsafe_allow_html=True)
    st.image(image)
    st.image(image2)
    st.image(image3)

    # st.markdown('''
    #     <p><span style=" font-weight: bold;">lorem </span>lorem</p>
    # ''', unsafe_allow_html=True)

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
