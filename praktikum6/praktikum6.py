# Import Library
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Header
st.title('Praktikum 06 Visualisasi Data')
st.write('KELOMPOK 16:')
st.markdown("""
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002
""")

# Dataset
stores= ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female= [120, 230, 170]

# Dataset Transaksi penjualan
stores= ['Store A', 'Store B', 'Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

# Data Querter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

# 1. Grafik Stacked Vertikal Bar Chart
st.subheader('1. Stacked Vertikal Bar Chart')

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='deepskyblue')
ax.bar(x, female, bottom= male, label='Female', color='pink')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 2. Grafik Stacked Vertikal Bar Chart
st.subheader('2. Stacked Vertikal Bar Chart dengan Matplotlib')

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='blueviolet')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='lime')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 3. Grafik Kostumisasi Stacked Vertikal Bar Chart
st.subheader('3. Kostumisasi Stacked Vertikal Bar Chart')

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_a[i]), ha='center', color='black')

st.pyplot(fig)

# 4. Grafik Multiple Stacked Vertikal Bar Chart
st.subheader('4. Multiple Stacked Vertikal Bar Chart')

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# Quarter 1
ax.bar(x-width/2, q1_male, label='Q1 male', color='cyan', width=width)
ax.bar(x-width/2, q1_female, bottom=q1_male, label='Q1 female', color='deeppink', width=width)

# Quarter 2
ax.bar(x+width/2, q2_male, label='Q2 male', color='steelblue', width=width)
ax.bar(x+width/2, q2_female, bottom=q2_male, label='Q2 female', color='tomato', width=width)

ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)