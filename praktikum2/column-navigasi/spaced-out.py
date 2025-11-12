import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("Spaced-out")
st.write("Kelompok: 16")
st.markdown("""
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002 
""")

img = Image.open("../../praktikum01/assets/jk_1.jpg")
st.title("Spaced Out Columns")
# Defining two rows
for _ in range(2):
# Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)