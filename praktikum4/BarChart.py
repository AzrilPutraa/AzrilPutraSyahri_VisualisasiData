import streamlit as st
import matplotlib.pyplot as plt

st.subheader('Praktikum 4 - Bar Chart')
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002
""")

# --- DATA AWAL ---
data = {
    'Jurusan': ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
    'Jumlah Mahasiswa': [120, 150, 100, 80]
}

# ==========================================
# BAGIAN 1: Kustomisasi Basic Bar Chart
# ==========================================
st.title("Kustomisasi Basic Bar Chart")

fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'purple']

# Simpan objek bar ke dalam variabel 'bars' agar bisa diakses nanti
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)

ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# --- Menambahkan nilai angka di atas batang ---
for bar in bars:
    height = bar.get_height() # Ambil tinggi batang
    # Tulis teks di posisi: x (tengah batang), y (tinggi + 5), nilai (string)
    ax.text(bar.get_x() + bar.get_width()/2, height + 5, str(height), ha='center')

st.pyplot(fig)


# ==========================================
# BAGIAN 2: Multiple Basic Bar Chart (2023 vs 2024)
# ==========================================
st.title("Multiple Basic Bar Chart")

# Data tambahan
data_2023 = [120, 150, 100, 80]
data_2024 = [140, 160, 110, 90]

x = range(len(data['Jurusan']))
width = 0.4

fig, ax = plt.subplots()

# Plot batang 2023 (Biru)
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')

# Plot batang 2024 (Oranye) - Digeser ke kanan sejauh 'width'
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Mengatur posisi label X di tengah-tengah dua batang
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(data['Jurusan']) # Memberi nama label sesuai jurusan

ax.legend() # Menampilkan legenda (kotak keterangan warna)

st.pyplot(fig)