    # import library yang dibutuhkan
import streamlit as st

# text element
st.header("Ini Header") # header - untuk membuat tulisan header
st.subheader("Ini sub header") # subheader - untuk membuat sub header
st.text("ini text biasa tanpa format") # text - untuk membuat text tanpa format
st.markdown("**ini text bold** dan *ini untuk text italic*") # markdown - untuk membuat text bold dan italic
st.markdown("""
- ini baris 1
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan markdown multibaris """)
st.caption("ini caption") # caption - untuk membuat caption
st.title("KELOMPOK 16 - VISUALISAI DATA ") # title - untuk membuat title

# coba mandiri
# tuliskan
# 1. judul praktikum pakai title()
# 2. bagian praktikum pakai subheader()
# 3. nama lengkap anggota - nim pakai markdown multibaris """

st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197 
""") 

# Bagian 2: Menampilkan Rumus (LaTeX)
st.header("Dispalying LaTeX")
st.latex(r'''\cos^\theta = 1-2\sin^2\theta ''')
st.latex(r'''  (a+b)^2 = a^2 + b^2 + 2ab ''')

# Bagian 3: Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

# simpan ke variable 
code = '''
def hello()
print("Hello, Streamlit!)
'''

# st.code() untuk?

st.code(code, language="python")

st.subheader("Java Code")
st.code("""
public class GFG {
        public static void main(String arg[]) {
        System.out.printIn("Hello World!);
        }
    }
""", language='java')


# Fungsi st.code

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
        adddlert("Welcome guest!); kesalahan ketik (adddleart) sengaja dibuat untuk menimbulkan error
        }

catch(err) {
        document.getElementById("demo").innerHTML = err.message; //
        }
""")