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


def show_penyakit_diabetes():

    st.markdown('''
    <header>
        <h1 style='text-align: center;'>Penyakit Diabetes</h1>
    </header>
    <section>
        <h3>Kasus Global Diabetes Melitus</h3>
        <p style='text-align: justify;'>Diabetes tidak hanya menyebabkan kematian prematur di seluruh dunia. Penyakit ini juga menjadi penyebab utama
            kebutaan, penyakit jantung, dan gagal ginjal. Organisasi International Diabetes Federation (IDF)
            memperkirakan sedikitnya terdapat 463 juta orang pada usia 20-79 tahun di dunia menderita diabetes pada
            tahun 2019 atau setara dengan angka prevalensi sebesar 9,3% dari total penduduk pada usia yang sama.
            Berdasarkan jenis kelamin, IDF memperkirakan prevalensi diabetes di tahun 2019 yaitu 9% pada perempuan dan
            9,65% pada laki-laki. Prevalensi diabetes diperkirakan meningkat seiring penambahan umur penduduk menjadi
            19,9% atau 111,2 juta orang pada umur 65-79 tahun. Angka diprediksi terus meningkat hingga mencapai 578 juta
            di tahun 2030 dan 700 juta di tahun 2045.</p>
    </section>
''', unsafe_allow_html=True)
    st.image(image)

    st.image(image2)

    st.markdown('''
     <p style="text-align: justify;">Negara di wilayah Arab-Afrika Utara, dan Pasifik Barat menempati peringkat
            pertama dan ke-2 dengan prevalensi diabetes pada penduduk umur 20-79 tahun tertinggi antara 7 regional di
            dunia, yaitu sebesar 12,2% dan 11,14%. Wilayah Asia Tenggara dimana indonesia berada, menempati peringkat
            ke-3 dengan prevalensi sebsar 11,3%. IDF juga memproyeksikan jumlah penderita diabetes pada penduduk umur
            20-79 tahun pada beberapa negara di dunia yang telah mengindentifikasi 10 negara dengan jumlah penederita
            teringgi. Cina, India, dan Amerika Serikat menempati urutan tiga teratas dengan jumlah penderita 116,4 juta,
            77 juta, dan 31 juta. Indonesia berada di peringkat ke-7 di antara 10 negara dengan jumlah penderita
            terbanyak, yaitu sebesar 10,7 juta. Indonesia menjadi satu-satunya negara di Asia Tenggara pada daftar
            tersebut, sehingga dapat diperkirakan besarnya kontribusi Indonesia terhadap prevalensi kasus diabetes di
            Asia Tenggara.</p>
    ''', unsafe_allow_html=True)

    st.markdown('''
   <h2>Definisi Kasus</h2>
        <p style="text-align: justify;">Diabetes adalah penyakit menahun (kronis) berupa gangguan metabolik yang ditandai dengan kadar gula darah
            yang melebihi batas normal. Penyebab kenaikan kadar gula darah tersebut menjadi landasan pengelompokkan
            jenis Diabetes Melitus
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
        <p><span style=" font-weight: bold;">Melitus tipe 2. </span>Diabetes yang disebabkan kenaikan gula darah karena
            penurunan sekreasi insulin
            yang rendah oleh kelenjar pankreas</p>
    ''', unsafe_allow_html=True)

    st.image(image4)

    st.markdown('''
         <p style="text-align: justify;"><span style="font-weight: bold;"> Diabetes Melitus tipe gestasional. </span> Diabetes tipe ini ditandai
            dengan kenaikan gula darah pada selama masa kehamilan. Gangguan ini biasanya terjadi pada minggu ke-24
            kehamilan dan kadar gula darah akan kembali normal setelah persalinan.</p>
        <p style="text-align: justify;">Penegakkan diagnosa diabetes melitus dilakukan dengan pengukuran kadar gula darah. Pemeriksaan gula darah
            yang dianjurkan adalah pemeriksaan secara enzimatik dengan menggunakan bahan plasma darah vena. Kriteria
            diagnosis diabetes melitus meliputi 4 hal, yaitu:</p>
        <ol style="text-align: justify;">
            <li>Pemeriksaan glukosa plasma puasa lebih dari atau sama dengan 126 mg/dl. Puasa adalah kondisi tidak ada
                asupan kalori selama minimal 8 jam</li>
            <li>Pemeriksaan glukosa plasma lebih dari atau sama dengan 200 mg/dl 2 jam setelah Tes Toleransi Glukosa
                Oral (TTGO) dengan beban glukosa 75 gram</li>
            <li>Pemeriksaan glukosa plasma sewaktu lebih dari atau sama dengan 200 mg/dl dengan keluhan klasik</li>
            <li>Pmeriksaan HbA1c lebih dari atau saam dengan 6,5% dengan menggunakan metode yang terstandardisasi oleh
                National Glychohaemoglobin Standardization Program (NGSP).</li>
        </ol>
        <p style="text-align: justify;">Hasil pemeriksaan yang tidak memenuhi kriteria normal maupun kriteria diabetes melitus maka digolonhkan ke
            dala kelompok prediabetes yang terdiri dari Toleransi Glukosa Terganggu (TGT) dan Glukosa Darah Puasa
            Terganggu (GDPT). GDPT terjadi ketika hasil pemeriksasan glukosa plasma puasa antara 100-125 mg/dl dan
            pemeriksaan TTGO glukosa plasma 2 jam < 140 mg/dl. TGT terpenuhi jika hasil pemeriksaan glukosa plasma 2 jam
                setelah TTGO antara 140-199 mg/dl dan glukosa plasma puasa < 100 mg/dl.</p>
    ''', unsafe_allow_html=True)
    st.image(image5)

    st.markdown('''
         <h2>Kasus Diabetes Melitus di Indonesia</h2>
        <p style="text-align: justify;">
            Riset Kesehatan Dasar (Riskesdas) yang dilaksanakan pada tahun 2018 melakukan pengumpulan data penderita
            diabetes melitus pada penduduk berumur lebih dari atau sama dengan 15 tahun. Kriteria diabetes melitus pada
            Riskesdas 2018 mengacu pada konsensus perkumpulan Endokrinologi Indonesia (PERKENI) yang mengadopsi kriteria
            American Diabetes Association (ADA). Menurut kriteria tersebut, diabetes melitus ditegakkan bila kadar
            glukosa darah puasa lebih dari atau saam dengan 126 mg/dl, atau glukosa darah 2 jam pasca pembebanan lebih
            dari atau sama dengan 200 mg/dl, atau glukosa darah sewaktu lebih dari atau sama dengan 200 mg/dl dengan
            gejala sering lapar, sering haus, sering buang air kecil dan dalam jumlah banyak, dan berat badan turun.
        </p>
        <p style="text-align: justify;">
            Hasil Riskesdas 2018 menunjukkan bahwa prevalensi diabetes melitus di indonesia berdasarkan diagnosis dokter
            pada umur >= 15 tahun sebesar 2%. Angka ini menunjukkan peningkatan dibandingkan
            prevalensi diabetes melitus pada penduduk >= 15 tahun pada hasil Riskesdas 2013 sebesar 1,5%. Namun
            prevalensi diabetes melitus menurut hasil pemeriksaan gula darah meningkat dari 6,9% pada 2013 menjadi 8,5%
            pada tahun 2018. Angka ini menunjukkan bahwa baru sekitar 25% penderita diabetes yang mengetahui bahwa
            dirinya menderita diabetes.
    ''', unsafe_allow_html=True)

    st.image(image6)
    st.markdown('''
        <p style="text-align: justify;">
            Hampir semua provinsi menunjukkan peningkatan prevalensi pada tahun 2013-2018, Kecuali provinsi Nusa
            Tenggara Timur. Terdapat empat provinsi dengan prevalensi teringgi pada tahun 2013 dan 2018, yaitu Di
            Yogyakarta,DKI Jakarta,Sulawesi Utara, dan Kalimantan Timur. Terdapat beberapa provinsi dengan peningkatan
            prevalensi tertinggi sebesar 0,9%, yaitu Riaum DKI Jakarta, Banten, Gorontalo, dan Papua Barat.
        </p>
        <p style="text-align: justify;">
            Gambaran prevalensi Diabetes menurut provinsi pada tahun 2018 juga menunjukkan bahwa provinsi Nusa Tenggara
            Timur memilki prevalensi terendah sebesar 0,9%, diikuti oleh Maluku dan Papua sebesar 1,1%. Gambaran di
            bawah ini merupakan prevalensi berdasarkan diagnosis dokter yang sangat ditentukan oleh keteraturan dan
            kepatuhan pencatatan rekam medis.
        </p>
    ''', unsafe_allow_html=True)
    st.image(image7)
    st.markdown('''
          <h2>Faktor Risiko Diabetes Melitus</h2>
        <p style="text-align: justify;">
            Seperti penyakit tidak menular lainnya, Diabetes Melitus juga memiliki faktor risiko atau faktor pencetus
            yang berkontribusi terhadap kejadian penyakit. Upaya pengendalian faktor risiko dapat mencegah diabetes
            melitus dan menurunkan tingkat fatalitas.
        </p>
        <p style="text-align: justify;">
            Faktor risiko diabetes terdiri dari faktor yang dapat dimodifikasi dan faktor yang tidak dapat dimodifikasi.
            Faktor risiko yang tidak dapat dimodifikasi adalah ras, etnikm umur, jenis kelamin, riwayat keluarga dengan
            diabetes melitus, riwayat melahirkan bayi > 4.000 gram, riwayat lahir dengan berat badan lahir rendah (BBLR
            atau < 2.500 gram). Faktor risiko yang dapat dimodfikasi yaitu berat badan lebih, obesitas abdominal/sentra,
                kurangnya aktifitas fisik, hipertensi, dislipidemia, diet tidak sehat dan tidak seimbang (tinggi
                kalori), kondisi preadiabetes yang ditandai dengan toleransi glukosa terganggu (TGT 140-199 mg/dl) atau
                gula rah puasa terganggu (GDPT < 140 mg/dl), dan merokok.</p>
    ''', unsafe_allow_html=True)
    st.image(image8)
    st.markdown('''
          <p style="text-align: justify;">
                    Pada Riskesdas 2018, prevalensi diabetes melitus pada perempuan lebih tinggi dibandingkan laki-laki
                    dengan perbandingan 1,78% terhadap 1,21%, dan Riskesdas 2013 prevalensi pada perempuan terhadap
                    laki-laki sebesar 1,7% terhadap 1,4%. Pada 5 tahun terakhir, prevalensi pada perempuan menunjukkan
                    sedikit peningkatan. Sedangkan prevalensi pada laki-laki menunjukkan penurunan.
                </p>
    ''', unsafe_allow_html=True)
    st.image(image9)
    st.markdown('''
         <p style="text-align: justify;">
                    Prevalensi diabetes melitus menunjukkan peningkatan seiring dengan bertambahnya umur penderita yang
                    mencapai puncaknya pada umur 55-64 tahun dan menurun setelah melewati rentang umur tersebut. Pola
                    peningkatan ini terjadi pada Riskesdas 2013 dan 2018 yang mengindikasikan semakin tinggi umur maka
                    semakin besar risiko untuk mengalami diabetes. Peningkatan prevalensi dari tahun 2013-2018 terjadi
                    pada kelompok umur 45-54 tahun, 65-74 tahun, dan >= 75 tahun.
                </p>
    ''', unsafe_allow_html=True)
    st.image(image10)
    st.markdown('''
        <p style="text-align: justify;">
                    Proporsi penderita diabetes melitus menurut tingkat pendidikan menunjukkan bahwa responden dengan
                    tingkat pendidikan tamat akademi/universitas memiliki proporsi tertinggi pada Riskesdas tahun 2013
                    dan Riskesdas tahun 2018, yaitu sebesar 2,5% dan 2,8%. Sedangkan responden dengan tingkat pendidikan
                    lebih rendah dari universitas/akademi memiliki prevelensi kurang dari 2%. Hal ini dapat diasumsikan
                    terkait dengan gaya hidup dan akses terhadap deteksi kasus di pelayanan kesehatan pada kelompok
                    dengan tingkat pendidikan akademi/universitas.
                </p>
    ''', unsafe_allow_html=True)
    st.image(image11)
    st.markdown('''
        <p style="text-align: justify;">
                    Penderita diabetes melitus pada responden yang tinggal di wilayah perkotaan lebih tinggi
                    dibandingkan yang tinggal di perdesaan, yaitu 2% berbanding 1% pada Riskesdas 2013 dan 1,89%
                    berbanding 1,01% pada Riskesdas 2018. Hal ini dapat diamsumsikan adanya akses terhadap deteksi kasus
                    di pelayanan kesehatan yang lebih baik pada wilayah perkotaan dibandingkan perdesaan.
                </p>
    ''', unsafe_allow_html=True)

    st.markdown('''
         <h2>Upaya Pencegahan dan Pengendalian Diaebetes Melitus</h2>
        <p style="text-align: justify;">
            Pencegahan dan pengendalian diabetes melitus di indonesia dilakukan agar individu yang sehat tetap sehat,
            orang yang sudah memiliki faktor risiko dapat mengendalikan faktor risiko agar tidak jatuh sakit diabetes,
            dan orang yang sudah menderita Diabetes Melitus dapat mengendalikan penyakitnya agar tidak terjadi
            komplikasi atau kematian dini. Upaya pencegahan dan pengendalian diabetes dilakukan melalui edukasi,deteksi
            dini faktor risiko PTM, dan tatalaksana sesuai standar.
        </p>
        <p style="text-align: justify;">
            Individu dengan riwayat Toleransi Glukosa Terganggu (TGT) atau Glukosa Darah Puasa (GDP) terganggu atau
            kelompok pre-diabetes seharusnya lebih mawas diri dan perlu untuk menerapkan pola hidup sehat dengan
            memperhatikan asupan makan dan minumnya, serta teratur untuk melakukan aktivitas fisik sehingga kondisi ini
            tidak berlanjut menjadi diabetes melitus.
        </p>
        <p style="text-align: justify;">
            Keterlibatan masyarakat melalui Upaya Kesehatan Berbasis Masyarakat (UKBM) juga memiliki peran penting dalam
            pengendalian diabetes melitus atau yang lebih dikenal dengan Posbindu. Melalui Posbindu ini, upaya deteksi
            dini sebagai identifikasi awal individu memiliki faktor risiko termasuk pemeriksaan gula darah sewaktu oleh
            para kader teraltih dapat dilakukan, sehingga bila ditemukan individu dengan masalah dapat dilakukan
            edukasi, intervensi dan atau dirujuk ke Fasilitas Pelayanan Kesehatan Tingkat Pertama (FKTP). Populasi
            dengan faktor risiko bisa memodifikasi gaya hidupnya sehingga bisa kembali ke kondisi normal melalui Gerakan
            Tekan Angka Obesitas (Gentas), Konseling Upaya Berhenti Merokok (UBM), melakukan aktivitas fisik secara
            teratur dan mengatur pola makan sesuai kondisi tubuh.
        </p>
    ''', unsafe_allow_html=True)
    st.image(image12)
    st.markdown('''
         <p style="text-align: justify;">
            Kondisi obesitas yaitu orang dengan indeks masa tubuh (IMT) >= 27 merupakan salah satu faktor risiko
            diabetes. Pada gambar di atas dapat kita ketahui bahwa prevalensi obesitas ternyata diiringi dengan
            peningkatan prevalensi diabetes melitus dari tahun 2013 sampai dengan 2018.
        </p>
        <p style="text-align: justify;">
            Pemerintah melalui peraturan pemerintah Nomor 2 tahun 2018, Peraturan Menteri Dalam Negri Nomor 100 tahun
            2018, dan peraturan Menteri Kesehatan Nomor 4 tahun 2019 telah menetapkan bahwa upaya pengendakuan diabetes
            melitus, merupakan salah satu pelayanan minimal yang wajib dilakukan oleh pemerintah daerah. Setiap
            penderita diabetes melitus akan menerima pelayanan sesuai standar minimal satu kali sebulan yang meliputi
            pengukuran kadar gula darah, edukasim dan terapi farmakologi serta rujukan jika diperlukan. Dengan adanya
            jaminan ini diharapkan semua penderita diabetes melitus bisa terkontrol dan menerima tatalaksana dengan baik
            guna menghindari komplikasi dan kematian dini serta bisa menurunkan beban biaya akibat diabetes melitus dan
            komplikasinya.
        </p>
        <p style="text-align: justify;">
            Selain itu, adanya Inpres No 1 tahun 2017 tentang Germas juga membantu mendorong pembudayaan perilaku hidup
            sehat bagi seluruh masyarakat termasuk orang dengan faktor risiko PTM dan penderita diabetes melitus.
            Keterlibatan semua sektor terkait dalam mendukung perwujudan Germas diharpkan dapat menurunkan prevalensi
            diabetes melitus dan faktor risikonya. Penggunaan obat dalam pengelolaan diabetes melitus melitus akan
            efektif bila disertai dengan modifikasi gaya hiduup yang lebih sehat terutama yang berkaitan dengan faktor
            risiko yang dimiliki.
        </p>
        <p style="text-align: justify;">
            Beberapa hal yang dilakukan dalam pengendalian diabetes melitus sebagai berikut: <br />
            <span style="font-weight: bold;">Pola Makan.</span><br />
            Pengaturan pola makan menyesuaikan dengan kebutuhan kalori yang dibutuhkan oleh penyandang diabetes melitus,
            dikombinasikan juga dengan aktivitas fisik hariannya sehingga tercukupi dengan baik. Pengaturan meliputi
            kandungan, kuantitas dan sewaktu asupan makanan (3 J- Jenis, Jumlah, Jadwal) agar penyandang diabetes
            melitus memiliki berat badan yang ideal dan gula darh dapat terkontrol dengan baik.
        </p>
    ''', unsafe_allow_html=True)
    st.image(image13)
    st.markdown('''
         <p style="text-align: justify;">
            Pola konsumsi makanan dan minuman manis yang merupakan salah satu faktor risiko diabetes melitus juga
            tergambar pada hasil Riskesdas 2018. Perilaku konsumi makanan manis menggambarkan bahwa sebagian besar
            responden mengkonsumsi 1-6 kali per minggu dengan prevalensi 47,8%, hanya 12% responden yang mengkonsumsi <
                3 kali per bulan. Gambaran berbeda terjadi pada pola konsumsi minuman manis, yaitu sebagian besar
                responden mengkonsumsi> 1 kali per hari sebesar 61,3%. Hanya 8,5% responden yang mengkonsumsi minuman
                manis < 3 kali per bulan. Tingginya prevalensi konsumsi makanan dan minuman manis dapat berkontribusi
                    terhadap tingginya kejadian diabetes. </p>
          <p style="text-align: justify;">
                        <span style="font-weight: bold;">Aktivitas Fisik.</span> <br />
                        Aktivitas fisik menyesuaikan dengan kemampuan tubuh, dikombinasikan juga dengan asupan makanan.
                        Aktivitas fisik dilakukan dengan durasi minimal 30 menit/hari atau 150 menit/minggu dengan
                        intensitas sedang (50-70% maximum heart rate). Target dari kegiatan ini berupa kepatuhan para
                        penyandang diabetes melitus untuk melakukan latihan fisik secara teratur sehingga tercapai berat
                        badan ideal dan gula darah dapat terkontrol dengan baik.
                    </p>          
    ''', unsafe_allow_html=True)
    st.image(image14)
    st.markdown('''
          <p style="text-align: justify;">
                        <span style="font-weight: bold;">Tatalaksana/Terapi Farmokologi.</span> <br />
                        Tatalaksana/terapi farmologi harus mengikuti anjuran dari dokter. Selain itu, penting bagi
                        penyandang diabetes melitus untuk memantau kadar gula darah secara berkala. Paling tidak setiap
                        6 bulan sekali penyandang diabetes dinilai/dievaluasi pengobatan dan gaya hidupnya untuk
                        mengontrol kepatuhan penyandang diabetes terhadap modifikasi gaya hidup. Dengan penilaian ini
                        diharapkan penyandang diabetes melitus menjadi lebih sehat serta mematuhi tatalaksana
                        farmakologi sehingga penyakitnya lebih terkontrol dan terkendali.
                    </p>
                    <p style="text-align: justify;">
                        <span style="font-weight: bold;">Pelibatan peran keluarga.</span> <br />
                        Keterlibatan keluarga untuk mendorong penyandang diabetes untuk patuh minum obat, berperilaku
                        hidup sehat, atau memodifikasi gaya hidupnya menjadi lebih sehat juga menjadi kunci keberhasilan
                        penyandang diabetes melitus untuk mengendalikan penyakitnya.
                    </p>       
    ''', unsafe_allow_html=True)


if __name__ == "__main__":
    show_penyakit_diabetes()
