import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Containers")
st.write("Kelompok: 16")
st.markdown("""
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002 
""")

st.title("Containers")
with st.container():
    st.write("Elements inside the container")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside the container")

st.title("Out of Order Container")

# Defining Containers
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")

# Now insert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))