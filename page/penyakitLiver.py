import streamlit as st
from PIL import Image

image = Image.open('img/gambar1.png')
image2 = Image.open('img/gambar2.png')
image3 = Image.open('img/gambar3.png')
image4 = Image.open('img/gambar4.png')
image5 = Image.open('img/gambar5.PNG')
image6 = Image.open('img/gambar6.PNG')
image7 = Image.open('img/gambar7.png')
image8 = Image.open('img/gambar8.png')
image9 = Image.open('img/gambar9.png')
image10 = Image.open('img/gambar10.png')
image11 = Image.open('img/gambar11.png')
image12 = Image.open('img/gambar12.png')
image13 = Image.open('img/gambar13.PNG')
image14 = Image.open('img/gambar14.PNG') 


def show_inform_liver():

    st.markdown('''
    <header>
        <h1 style='text-align: center;'>Penyakit Liver / Hepatitis</h1>
    </header>
    <section>
        <h3>Kasus Global Diabetes Melitus</h3>
        <p style='text-align: justify;'>lorem dlu aja ya</p>
    </section>
''', unsafe_allow_html=True)
    st.image(image)

    st.image(image2)

    st.markdown('''
     <p style="text-align: justify;">lorem dlu aja ya</p>
    ''', unsafe_allow_html=True)

    st.markdown('''
   <h2>Definisi Kasus</h2>
        <p style="text-align: justify;">lorem dlu
        </p>
        <p  style="text-align: justify;"><span style="font-weight: bold;">Diabetes Melitus tipe 1. </span>Diabetes yang disebabkan kenaikan kadar gula
            darah
            karena kerusakan sel beta
            pankreas sehingga produksi insulin tidak ada sama sekali. Insulin adalah hormon yang dihasilkan oleh
            pancreas untuk mencerna gula dalam darah. Penderita diabetes tipe ini membutuhkan asupan insulin dari luar
            tubuhnya.</p>
    ''', unsafe_allow_html=True)

    st.image(image3)

    st.markdown('''
        <p><span style=" font-weight: bold;">lorem </span>lorem</p>
    ''', unsafe_allow_html=True)

    st.image(image4)

    st.markdown('''
         <p style="text-align: justify;"><span style="font-weight: bold;"> lorem </span> lorem</p>
        <p style="text-align: justify;">lorem:</p>
        <ol style="text-align: justify;">
            <li>Plorem</li>
            
        </ol>
        <p style="text-align: justify;">lorem</p>
    ''', unsafe_allow_html=True)
    st.image(image5)

    st.markdown('''
         <h2>Kasus Diabetes Melitus di Indonesia</h2>
        <p style="text-align: justify;">
           lorem
        </p>
        <p style="text-align: justify;">
           lorem
    ''', unsafe_allow_html=True)

    st.image(image6)
    st.markdown('''
        <p style="text-align: justify;">
            lorem
        </p>
        <p style="text-align: justify;">
            lorem
        </p>
    ''', unsafe_allow_html=True)
    st.image(image7)
    st.markdown('''
          <h2>Faktor Risiko Diabetes Melitus</h2>
        <p style="text-align: justify;">
            Slorem
        </p>
        <p style="text-align: justify;">
            lorem</p>
    ''', unsafe_allow_html=True)
    st.image(image8)
    st.markdown('''
          <p style="text-align: justify;">
                    lorem
                </p>
    ''', unsafe_allow_html=True)
    st.image(image9)
    st.markdown('''
         <p style="text-align: justify;">
                    lorem
                </p>
    ''', unsafe_allow_html=True)
    st.image(image10)
    st.markdown('''
        <p style="text-align: justify;">
                    lorem
    ''', unsafe_allow_html=True)
    st.image(image11)
    st.markdown('''
        <p style="text-align: justify;">
                   lorem
                </p>
    ''', unsafe_allow_html=True)

    st.markdown('''
         <h2>Upaya Pencegahan dan Pengendalian Diaebetes Melitus</h2>
        <p style="text-align: justify;">
            lorem
        </p>
        <p style="text-align: justify;">
            lorem
        </p>
        <p style="text-align: justify;">
           lorem
        </p>
    ''', unsafe_allow_html=True)
    st.image(image12)
    st.markdown('''
         <p style="text-align: justify;">
           lorem
        </p>
        <p style="text-align: justify;">
            lorem
        </p>
        <p style="text-align: justify;">
           lorem
        </p>
        <p style="text-align: justify;">
            Blorem
        </p>
    ''', unsafe_allow_html=True)
    st.image(image13)
    st.markdown('''
         <p style="text-align: justify;">
            lorem</p>
          
           
    ''', unsafe_allow_html=True)
   


if __name__ == "__main__":
    show_penyakit_diabetes()
