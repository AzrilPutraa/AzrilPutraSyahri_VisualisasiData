# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 

st.caption("Praktikum 1") # caption - untuk membuat caption
st.title("KELOMPOK 16 - VISUALISAI DATA ") # title - untuk membuat title

# coba mandiri
# tuliskan
# 1. judul praktikum pakai title()
# 2. bagian praktikum pakai subheader()
# 3. nama lengkap anggota - nim pakai markdown multibaris """

st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197 
""")

# DataFrame : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("Data Frame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# menampilkan dataframe
st.dataframe(df)

# Highlight Nilai Minimum
st.subheader("Highlight Minimum Value di DataFrame")

#
#
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis 
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)
# Menampilkan       
st.table(df)

# Metric: komponen tampilan angka
st.subheader("Metrics")
# Menampilkan Tunggal

# Metrics Tunggal
st.metric(label="Temperatur", value="31 °C", delta="1.2 °C")

# Metrics 
# delta color

# definisikan

col1, col2, col3, = st.columns(3)

#Menampilkan indikator

col1.metric("Curah Hujan", "100 cm", "10cm")
col2.metric(label="Populasi", value="123 Miliiyar", delta="1.2 Miliyar", delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta="10", delta_color="off")

# Menampilkan metrik
st.metric(label="Speed", value=None, delta="-")

