# Buttons and Sliders
# Buttons and Sliders dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna untuk berinteraksi dengan aplikasi. Elemen-elemen ini digunakan untuk mengumpulkan input dari pengguna atau mengontrol parameter secara langsung dalam aplikasi Streamlit.

# Bagian 1
# Buttons 
# Buttons dalam Streamlit adalah elemen interaktif yang digunakan untuk memicu suatu aksi ketika pengguna mengklik tombol tersebut.
import streamlit as st

st.title('Creating a Button')

# Defining a Button
button = st.button('Click Here')

if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')


# Bagian 2
# Radio Buttons 
# Radio Buttons dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna memilih salah satu opsi dari beberapa pilihan yang tersedia.
import streamlit as st

st.title('Creating Radio Buttons')

# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others')
)

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write('You have selected Female.')
else:
    st.write("You have selected Others.")


# Bagian 3
# Check Boxes
# Check Boxes dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna untuk memilih atau tidak memilih opsi tertentu.
import streamlit as st

st.title('Creating Checkboxes')
st.write('Select your Hobbies:')

# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')


# Bagian 4
# Drop-Downs
# Drop-Downs dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna memilih satu opsi dari daftar pilihan yang tersedia.
import streamlit as st

st.title('Creating Dropdown')

# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))


# Bagian 5
# Multiselects
# Multiselects dalam Streamlit adalah elemen interaktif yang memungkinkan pengguna memilih beberapa opsi dari daftar yang tersedia.
import streamlit as st

st.title('Multi-Select')

# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)


# Bagian 6
# Download Buttons 
# Download Buttons dalam Streamlit adalah elemen yang memungkinkan pengguna untuk mengunduh file langsung dari aplikasi.
import streamlit as st

st.title("Download Gambar")

# --- Tombol untuk animal1.jpg ---
st.download_button(
    label="Download animal1.jpg",
    data=open("assets/animal1.jpg", "rb"),
    file_name="animal1.jpg",
    mime="image/jpg"
)

# --- Tombol untuk animal2.jpg ---
st.download_button(
    label="Download animal2.jpg",
    data=open("assets/animal2.jpg", "rb"),
    file_name="animal2.jpg",
    mime="image/jpg"
)

# --- Tombol untuk animal3.jpg ---
st.download_button(
    label="Download animal3.jpg",
    data=open("assets/animal3.jpg", "rb"),
    file_name="animal3.jpg",
    mime="image/jpg"
)

# --- Tombol untuk animal4.jpg ---
st.download_button(
    label="Download animal4.jpg",
    data=open("assets/animal4.jpg", "rb"),
    file_name="animal4.jpg",
    mime="image/jpg"
)

# --- Tombol untuk animal5.jpg ---
st.download_button(
    label="Download animal5.jpg",
    data=open("assets/animal5.jpg", "rb"),
    file_name="animal5.jpg",
    mime="image/jpg"
)


# Bagian 7
# Progress Bars 
# Progress Bars dalam Streamlit adalah elemen visual yang digunakan untuk menunjukkan progres atau kemajuan dari suatu proses di aplikasi Anda.
import streamlit as st
import time

st.title('Progress Bar')

# Defining Progress Bar
download = st.progress(0)

for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)

st.write('Download Complete')


# Bagian 8
# Spinners 
# Spinners dalam Streamlit adalah elemen visual yang digunakan untuk memberikan indikasi bahwa suatu proses sedang berlangsung.
import streamlit as st
import time

st.title('Spinner')

# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)

st.write('Hello Kelompok 16 Visualisasi Data')

