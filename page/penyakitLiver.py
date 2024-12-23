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
        <p style='text-align: justify;'>Gejala hepatitis dapat bervariasi, namun yang paling umum menurut <a href="    https://www.unicef.org/indonesia/id/hepatitis-akut-berat-yang-belum-diketahui-penyebabnya-di-kalangan-anak-anak?gad_source=1&gclid=CjwKCAiAjp-7BhBZEiwAmh9rBUo7vt5nfnPoRCuKl1rEOCs8Quoath-ON7swfsTC0vCrlwnwitBuyxoCZxwQAvD_BwE
"> UNICEF  </a> meliputi:</p>
        </section>
''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1 :
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
    
    st.markdown('''
    <section>
        <h3>Pencegahan Penyakit Hepatitis </h3>
        <h4>1. Vaksinasi </h4>
        <p style='text-align: justify;'>Vaksin hepatitis A dan B tersedia dan sangat efektif dalam mencegah infeksi.</p>
        <p style='text-align: justify;'>Vaksinasi direkomendasikan untuk semua bayi, anak-anak, dan orang dewasa yang berisiko tinggi.</p>
        </section>
    <section>           
        <h4>2. Praktik Higiene yang Baik </h4>
        <p style='text-align: justify;'>Cuci tangan dengan sabun dan air bersih secara teratur, terutama sebelum makan atau menyiapkan makanan.</p>
        <p style='text-align: justify;'>Hindari makan makanan atau minum air yang mungkin terkontaminasi, terutama saat bepergian ke daerah dengan sanitasi yang buruk.</p>
        </section>
''', unsafe_allow_html=True)
    st.markdown('''
        <section>
            <h3>Pencegahan Penyakit Hepatitis</h3>
            
            <h3>1. Vaksinasi</h3>
            <p>
                <span>Vaksin hepatitis A dan B tersedia dan sangat efektif dalam mencegah infeksi.</span>
                <span>Vaksinasi direkomendasikan untuk semua bayi, anak-anak, dan orang dewasa yang berisiko tinggi.</span>
            </p>

            <h3>2. Praktik Higiene yang Baik</h3>
            <p>
                <span>Cuci tangan dengan sabun dan air bersih secara teratur, terutama sebelum makan atau menyiapkan makanan.</span>
                <span>Hindari makan makanan atau minum air yang mungkin terkontaminasi, terutama saat bepergian ke daerah dengan sanitasi yang buruk.</span>
            </p>

            <h3>3. Hindari Kontak dengan Darah dan Cairan Tubuh</h3>
            <p>
                <span>Gunakan sarung tangan saat memberikan pertolongan pertama atau membersihkan darah.</span>
                <span>Jangan berbagi sikat gigi, alat cukur, atau barang pribadi lainnya yang mungkin terkontaminasi darah.</span>
            </p>

            <h3>4. Praktik Seks yang Aman</h3>
            <p>
                <span>Gunakan kondom secara konsisten dan benar saat berhubungan seks.</span>
                <span>Batasi jumlah pasangan seksual dan hindari berhubungan seks dengan orang yang terinfeksi hepatitis B atau C.</span>
            </p>

            <h3>5. Hindari Penggunaan Narkoba Suntik</h3>
            <p>
                <span>Jangan pernah berbagi jarum suntik, alat suntik, atau peralatan lainnya yang digunakan untuk menyuntikkan narkoba.</span>
            </p>

            <h3>6. Skrining dan Pengujian</h3>
            <p>
                <span>Lakukan skrining hepatitis B dan C jika Anda berisiko tinggi, seperti memiliki riwayat transfusi darah, tato, atau tindik.</span>
                <span>Ibu hamil harus menjalani skrining hepatitis B untuk mencegah penularan ke bayi mereka saat lahir.</span>
            </p>
            </section>
''', unsafe_allow_html=True)


            # st.markdown('''
            #     <section>
            #         <h3>Bagaimana cara menjegah penyakit hepatitis? </h3>
            #         <p style='text-align: justify;'>Gejala hepatitis dapat bervariasi, namun yang paling umum menurut <a href="    https://www.unicef.org/indonesia/id/hepatitis-akut-berat-yang-belum-diketahui-penyebabnya-di-kalangan-anak-anak?gad_source=1&gclid=CjwKCAiAjp-7BhBZEiwAmh9rBUo7vt5nfnPoRCuKl1rEOCs8Quoath-ON7swfsTC0vCrlwnwitBuyxoCZxwQAvD_BwE
            # "> UNICEF  </a> meliputi:</p>
            #         </section>
            # ''', unsafe_allow_html=True)
            # col3,col4 = st.columns(2)
            # with col3 :
            #                         st.write("""
            #                         - Kelelahan
            #                         - Mual dan muntah
            #                         - Nyeri perut
            #                         - Urin berwarna gelap
            #                         """)

            # with col4:
            #                         st.write("""
            #                         - Feses berwarna pucat
            #                         - Kulit dan mata kuning (jaundice)
            #                         - Demam
            #                         - Nyeri sendi
            #                         """)



if __name__ == "__main__":
    # show_penyakit_diabetes()
    show_inform_liver()
