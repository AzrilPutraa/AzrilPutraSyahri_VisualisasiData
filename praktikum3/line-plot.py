import streamlit as st
import matplotlib.pyplot as plt

# Buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Layout Streamlit
st.title('Visualisasi Data Penjualan Produk')
st.sidebar.header('Pengaturan Grafik')
option = st.sidebar.selectbox('Pilih Tipe Visualisasi', ('Single Line Plot',
                                                        'Multiple & Customizations',
                                                        'Jenis Garis untuk Mununjukkan Tren',
                                                        'Subplot'))

# Identitas Kelompok
st.subheader('Praktikum 3 - Matplotlib Line Chart')
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A')
    ax.set_title('Penjualan Poduk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig)

# Multiple Line Plot & Customizations
def customize_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='red', linestyle='-', marker='x')

    ax.set_title('Penjualan Poduk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Jenis garis untuk Tren
product_C_sales = [18, 22, 25, 28, 32, 38, 42, 45, 48, 52, 56, 60]
product_D_sales = [7, 9, 11, 13, 16, 18, 20, 23, 25, 28, 30, 33]

def tren_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product C', color='green', linestyle='-.')
    ax.plot(months, product_B_sales, label='Product D', color='purple', linestyle=':')

    ax.set_title('Penjualan Poduk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Subplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot pertama untuk produk C
    axs[0].plot(months, product_C_sales, label='Product C', linestyle=':', color='green', marker='d')
    axs[0].set_title('Penjualan Produk C Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

# Plot pertama untuk produk D
    axs[1].plot(months, product_D_sales, label='Product D', linestyle=':', color='purple', marker='s')
    axs[1].set_title('Penjualan Produk D Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)


# Logika untuk menampilkan visualisasi sesuai menu
if option == 'Single Line Plot' :
    line_plot()
elif option == 'Multiple & Customizations' :
    customize_plot()
elif option == 'Jenis Garis untuk Mununjukkan Tren' :
    tren_line_plot()
elif option == 'Subplot' :
    subplots()  
