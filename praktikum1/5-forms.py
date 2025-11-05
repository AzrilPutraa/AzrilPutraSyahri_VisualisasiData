# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 5-froms")
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- BAGUS ACHMAD HIDAYAT - 0110222002
- AZRIL PUTRA SYAHRI - 0110222197
""")

# Froms pada streamlit adalah elemen yang memungkinkan pengguna untuk mengelompokkan berbagai input (seperti teks, angka, checkbox, dan lainnya) dalam satu unit. 

# Text Box pada streamlit adalah elemen input yang memungkinkan pengguna untuk memasukkan teks. 
st.title('Text Box')
# Creating Text Box
name = st.text_input('Enter your Name')
st.write('Your Name is', name) 

# Text Area pada streamlit adalah  elemen input yang digunakan untuk menerima masukan teks panjang dari pengguna.
st.title('Text Area')
# Creating Text Area
input_text = st.text_area('Enter your Review')
# Printing entered text
st.write("""You entered: \n""",input_text)

# Number Input pada streamlit adalah elemen input yang memungkinkan pengguna untuk memasukkan angka.
st.title('Number Input')
#Creating number input
st.number_input('Enter your Number')
# Creating number input
num = st.number_input('Enter your Number', 0, 10, 5, 2)
st.write('Min. Value is 0, /n Max. Value is 10')
st.write('Default Value is 5, /n Step Size value is 2')
st.write('Total value after adding Number entered with step value is:', num)

# Time input pada streamlit adalah  input yang memungkinkan pengguna untuk memilih waktu tertentu (jam dan menit).
st.title('Time')
# Defining Time Function
st.time_input('Select your Time')

# Date input pada streamlit adalah elemen yang memungkinkan pengguna untuk memilih tanggal tertentu melalui antarmuka interaktif. 
st.title('Date')
# Defining Date Function
st.date_input('Select Date')

import datetime
st.title('Date')
# Defining Time Function
st.date_input('Select your Date', value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

# Color input pada streamlit adalah elemen yang memungkinkan pengguna memilih warna melalui antarmuka pemilih warna (color picker). 
st.title('Select Color')
# Defining Color picker
color_code = st.color_picker('Select your Color')
st.header(color_code)

# Dataset Upload pada streamlit adalah fitur yang memungkinkan pengguna mengunggah file (seperti dataset) ke aplikasi Streamlit untuk diproses atau dianalisis. 
st.title('CSV Data')
data_file = st.file_uploader('Upload CSV', type=['csv'])
details = st.button('Check Details')
if details:
    if data_file is not None:
        file_details = {'file_name':data_file.name, 'file_type':data_file.type,
        'file_size':data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write('No CSV File is Upload')

# Submit Button pada streamlit adalah elemen yang digunakan untuk mengirimkan atau memproses data dalam sebuah formulir (form). 
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)
