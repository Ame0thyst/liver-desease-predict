# import streamlit as st
# import pandas as pd


# def show_dashboard():
#     st.title("Dashboard Data Liver")
#     st.write("Unggah dataset untuk mulai eksplorasi data berdasarkan atribut yang tersedia.")

#     # File uploader untuk dataset
#     uploaded_file = st.file_uploader("Unggah file dataset (CSV)", type="csv")

#     # Pastikan file diunggah sebelum melanjutkan
#     if uploaded_file is not None:
#         try:
#             # Membaca dataset langsung dari file yang diunggah
#             df = pd.read_csv(uploaded_file)

#             # Tampilkan info dataset
#             st.success("Dataset berhasil dimuat!")
#             st.write("Berikut adalah beberapa baris dari dataset:")
#             st.dataframe(df.head())

#             # Dropdown untuk memilih atribut
#             attributes = [
#                 'age_of_the_patient',
#                 'gender_of_the_patient',
#                 'total_bilirubin',
#                 'direct_bilirubin',
#                 'alkphos_alkaline_phosphotase',
#                 'sgpt_alamine_aminotransferase',
#                 'sgot_aspartate_aminotransferase',
#                 'total_protiens',
#                 'alb_albumin',
#                 'a_g_ratio_albumin_and_globulin_ratio',
#                 'result'
#             ]

#             # Sidebar untuk pengaturan chart
#             st.sidebar.header("Pengaturan Chart")
#             chart_type = st.sidebar.radio("Pilih jenis chart:", ["Line Chart", "Area Chart"])
#             x_axis = st.sidebar.selectbox("Pilih atribut X-axis:", attributes)
#             y_axis = st.sidebar.selectbox("Pilih atribut Y-axis:", attributes)

#             # Menampilkan chart jika atribut dipilih
#             if x_axis and y_axis:
#                 st.write(f"### {chart_type} untuk {y_axis} terhadap {x_axis}")
#                 chart_data = df[[x_axis, y_axis]].dropna()

#                 # Line Chart
#                 if chart_type == "Line Chart":
#                     st.line_chart(chart_data.rename(columns={x_axis: "X-axis", y_axis: "Y-axis"}))
#                 # Area Chart
#                 elif chart_type == "Area Chart":
#                     st.area_chart(chart_data.rename(columns={x_axis: "X-axis", y_axis: "Y-axis"}))
#             else:
#                 st.warning("Pilih atribut X dan Y untuk melihat visualisasi data.")

#         except Exception as e:
#             st.error(f"Gagal memuat dataset. Pastikan file berformat CSV dan benar. Error: {e}")
#     else:
#         st.warning("Silakan unggah file dataset untuk memulai.")


# # Untuk menjalankan fungsi dashboard
# if __name__ == "__main__":
#     show_dashboard()

import streamlit as st
import pandas as pd


def show_dashboard():
    st.title("Dashboard Data Liver")
    st.write("Unggah dataset untuk mulai eksplorasi data berdasarkan atribut yang tersedia.")

    # File uploader untuk dataset
    uploaded_file = st.file_uploader("Unggah file dataset (CSV)", type="csv")

    # Pastikan file diunggah sebelum melanjutkan
    if uploaded_file is not None:
        try:
            # Membaca dataset langsung dari file yang diunggah
            df = pd.read_csv(uploaded_file)

            # Tampilkan info dataset
            st.success("Dataset berhasil dimuat!")
            st.write("Berikut adalah beberapa baris dari dataset:")
            st.dataframe(df.head())

            # Dropdown untuk memilih atribut berdasarkan kolom yang ada di dataset
            attributes = list(df.columns)

            # Sidebar untuk pengaturan chart
            st.sidebar.header("Pengaturan Chart")
            chart_type = st.sidebar.radio("Pilih jenis chart:", ["Line Chart", "Area Chart"])
            x_axis = st.sidebar.selectbox("Pilih atribut X-axis:", attributes)
            y_axis = st.sidebar.selectbox("Pilih atribut Y-axis:", attributes)

            # Menampilkan chart jika atribut dipilih
            if x_axis and y_axis:
                st.write(f"### {chart_type} untuk '{y_axis}' terhadap '{x_axis}'")
                chart_data = df[[x_axis, y_axis]].dropna()

                # Line Chart
                if chart_type == "Line Chart":
                    st.line_chart(chart_data.rename(columns={x_axis: x_axis, y_axis: y_axis}))
                # Area Chart
                elif chart_type == "Area Chart":
                    st.bar_chart(chart_data.rename(columns={x_axis: x_axis, y_axis: y_axis}))
            else:
                st.warning("Pilih atribut X dan Y untuk melihat visualisasi data.")

        except Exception as e:
            st.error(f"Gagal memuat dataset. Pastikan file berformat CSV dan benar. Error: {e}")
    else:
        st.warning("Silakan unggah file dataset untuk memulai.")


# Untuk menjalankan fungsi dashboard
if __name__ == "__main__":
    show_dashboard()
