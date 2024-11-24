import streamlit as st
import pandas as pd
import numpy as np


def show_dashboard():
    st.title("Dashboard Data Liver")
    st.write("Gunakan chart di bawah untuk eksplorasi data berdasarkan atribut yang tersedia.")

    # Load data
    data_file = '../dataset/smote.csv'  # Pastikan file sudah ada
    if not data_file or not st.file_uploader:
        st.warning("Tidak ada data untuk ditampilkan. Pastikan dataset tersedia.")
        return

    # Baca dataset
    df = pd.read_csv(data_file)

    # Dropdown untuk memilih atribut
    attributes = [
        'age',
        'total_bilirubin',
        'direct_bilirubin',
        'alkphos',
        'sgpt',
        'sgot',
        'total_proteins',
        'albumin',
        'ag_ratio'
    ]

    st.sidebar.header("Pengaturan Chart")
    chart_type = st.sidebar.radio("Pilih jenis chart:", ["Line Chart", "Area Chart"])
    x_axis = st.sidebar.selectbox("Pilih atribut X-axis:", attributes)
    y_axis = st.sidebar.selectbox("Pilih atribut Y-axis:", attributes)

    if x_axis and y_axis:
        st.write(f"### {chart_type} untuk {y_axis} terhadap {x_axis}")
        chart_data = df[[x_axis, y_axis]].dropna()

        # Line Chart
        if chart_type == "Line Chart":
            st.line_chart(chart_data.rename(columns={x_axis: "X-axis", y_axis: "Y-axis"}))
        # Area Chart
        elif chart_type == "Area Chart":
            st.area_chart(chart_data.rename(columns={x_axis: "X-axis", y_axis: "Y-axis"}))

    else:
        st.warning("Pilih atribut X dan Y untuk melihat visualisasi data.")
