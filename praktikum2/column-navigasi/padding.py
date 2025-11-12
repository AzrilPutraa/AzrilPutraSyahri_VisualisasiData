import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("Padding")
st.write("Kelompok: 16")
st.markdown("""
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002 
""")

img = Image.open("../../praktikum01/assets/jk_1.jpg")
st.title("Padding")
# Defining Padding with Columns
col1, padding, col2 = st.columns([10, 2, 10])
with col1:
    col1.image(img)
with col2:
    col2.image(img)