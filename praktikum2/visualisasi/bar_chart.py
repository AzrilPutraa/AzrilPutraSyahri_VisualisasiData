import streamlit as st
import pandas as pd
import numpy as np 

st.title("Bar Chart")
st.write("Kelompok: 16")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197 
""")

df = pd.DataFrame(
    np.random.randn(40,4),
    columns=("C1", "C2", "C3", "C4")
)
st.bar_chart(df)