import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Empty Containers")
st.write("Kelompok: 16")
st.markdown("""
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002 
""")

# Empety Container
with st.container():
    for second in range(5):
        st.write(f"⏳ {second} seconds have passed")
        time.sleep(1)
        st.write("✓ Times up!!!")