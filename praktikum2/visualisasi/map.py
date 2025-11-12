import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 Visualisasi Data")
st.write("Kelompok: 16")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197 
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=("latitude", "longitude")
)

st.map(df)