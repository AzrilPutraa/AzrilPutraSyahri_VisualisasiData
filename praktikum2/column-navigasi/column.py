import streamlit as st
 

st.title("Columns")
st.write("Kelompok: 16")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197 
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image.open("../../praktikum/assets/animal2.jpg")
col2.write("Ini adalah kolom kedua")
