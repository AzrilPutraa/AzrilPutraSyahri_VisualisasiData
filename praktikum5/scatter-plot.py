import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Dataset Utama
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan =[50, 60, 70, 90, 100, 110, 130, 150, 180]

# Dataset Tambahan (Dataset Penjualan)
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# Data Untuk Analisis
data = {
    'Suhu' : [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat' : [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila' : [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan_Stroberi' : [40,50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan' :  [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Layout Utama
st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header('Pengaturan Visualisasi')

# Menu di Sidebar
option = st.sidebar.selectbox(
    'Pilih Contoh Scatter Plot',
    (
        'Basic Scatter Plot',
        'Kustomisasi Scatter Plot',
        'Multiple Scatter Plot',
        'Analisis Scatter Plot',
    )
)

st.caption('Praktikum 5 - Matplotlib Scatter Plot')
st.markdown("""
KELOMPOK 16 Visualisasi Data
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002
""")

# 1 Basic Scatter Plot
def basic_scatter():
    st.subheader('1. Basic Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2. Kustomisasi Scatter Plot
def customi_scatter():
    st.subheader('2. Kustomisasi Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='navy', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 3. Multiple Scatter Plot
def multiple_scatter():
    st.subheader('3. Multiple Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='lime', label='Hari Kerja', s=100)
    ax.scatter(suhu, penjualan_weekend, color='magenta', label='Akhir Pekan', s=100)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig) 

# 4. Analisis dengan Scatter Plot
def scatter_3_variable():
    st.subheader('4. Analisis dengan Scatter Plot')

    # Opsi Jenis Es Krim
    jenis_eskrim = st.selectbox('Pilih Jenis Es Krim', ['Cokelat', 'Vanila', 'Stroberi'])

    # Logika Untuk Opsi Jenis Es Krim Berdasarkan Rasa
    if jenis_eskrim == 'Coklat':
        penjualan = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        penjualan = df['Penjualan_Vanila']
    else:
        penjualan = df['Penjualan_Stroberi']

    st.subheader('Data Penjualan dan Suhu')
    st.dataframe(df)

    # Scatter Plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s =100, cmap='coolwarm', alpha=0.7)

    # Styling
    ax.set_title(f'Hubungan Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='Kelembapan (%)')
    st.pyplot(fig)

    # Ringkasan Hubungan
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik Menunjukan Hubungan Antara Suhu, Kelembapan, dan Penjualan Es Krim Jenis **{jenis_eskrim}**')

# Routing Berdasarkan Menu Sidebar
if option == 'Basic Scatter Plot':
    basic_scatter()
elif option == 'Kustomisasi Scatter Plot':
    customi_scatter()
elif option == 'Multiple Scatter Plot':
    multiple_scatter()
elif option == 'Analisis Scatter Plot':
   scatter_3_variable()
