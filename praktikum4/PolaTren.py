import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.subheader('Praktikum 4 - Pola Tren Dengan Bar Chart')
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002
""")

# Data jumlah mahasiswa per jurusan selama 5 tahun
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

# Membuat dataframe untuk visualisasi
df = pd.DataFrame(data)

# Streamlit 
st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

# Menambahkan filter tahun
# default=df['Tahun'] artinya secara otomatis semua tahun terpilih di awal
filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

# Menambahkan filter jurusan
jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)


# Cek agar error tidak muncul jika user menghapus semua pilihan
if not filter_tahun or not filter_jurusan:
    st.warning("Mohon pilih setidaknya satu Tahun dan satu Jurusan.")
else:
    # Filter data berdasarkan input pengguna
    # Kita ambil baris yang tahunnya sesuai, lalu kolomnya cuma 'Tahun' + jurusan yang dipilih
    filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]

    # Menampilkan data tabel
    st.subheader("Data Jumlah Mahasiswa")
    st.dataframe(filtered_data)

    # Membuat Bar Chart dengan filter
    st.subheader("Bar Chart dengan Filter")
    
    # Siapkan kanvas gambar
    fig, ax = plt.subplots(figsize=(10, 6))

    # Membuat Bar Chart berdasarkan data yang difilter
    x = range(len(filtered_data['Tahun']))
    width = 0.2  # Lebar batang

    # Looping untuk membuat batang setiap jurusan yang dipilih
    for i, jur in enumerate(filter_jurusan):
        # Rumus [p + i * width for p in x] digunakan agar batang berjejer ke samping, tidak menumpuk
        ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

    # Menyesuaikan sumbu dan judul
    ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Jumlah Mahasiswa")

    # Mengatur posisi label tahun agar berada tepat di tengah-tengah grup batang
    # Rumus matematika ini menghitung titik tengah berdasarkan jumlah jurusan yang dipilih
    center_pos = [p + width * len(filter_jurusan) / 2 - width / 2 for p in x]
    
    ax.set_xticks(center_pos)
    ax.set_xticklabels(filtered_data['Tahun'])
    
    ax.legend()

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
