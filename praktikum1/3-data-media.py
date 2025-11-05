# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 3-data-media")
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- BAGUS ACHMAD HIDAYAT - 0110222002
- AZRIL PUTRA SYAHRI - 0110222197
""")

# Images pada streamlit digunakan untuk menampilkan gambar i aplikasi secara mudah dan fleksibel.
st.write('Displayin an Images')
# Displaying Image by specifying path
st.image('assets/jk_0.jpg')
# Image Courtesy by unplash
st.write('Image Courtesy: unpalsh.com')

# Image Courtesy
st.write('Displaying Multiple Images')
# Listing out jk images
person_images = [
'assets/jk_1.jpg',
'assets/jk_2.jpg',
'assets/jk_3.jpg',
'assets/jk_4.jpg',
] 
# Displaying Multiple images with width 150
st.image(person_images, width=150)
# Image Courtesy
st.write('Image Courtesy : Unplash')

# Background Image dengan menggunakan CSS kustom.
import base64
# Function to  set Image as Backgroud
def add_local_background_image_(image):
    with open(image, 'rb') as image:
        encoded_string = base64.b64encode(image.read())
    st.write('Image Courtesy: unplash')
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:files/{'jpg'};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write('Background Image')
# Calling Image in function
add_local_background_image_('assets/jk_bg.jpg')

# Resizing an Image pada streamlit berarti mengubah ukuran gambar yang ditampilkan menggunakan fungsi st.image.
from PIL import Image

original_image = Image.open('assets/jk_1.jpg')
#Displaying Original Image
st.title('Original Image')
st.image(original_image)
# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title('Resized Image')
st.image(resized_image)
