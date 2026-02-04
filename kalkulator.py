import streamlit as st

st.set_page_config(page_title="Kalkulator", layout="centered")

st.markdown("""
<style>
    .block-container {
        max-width: 350px;
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
        height: 65px;
        font-size: 24px;
        font-weight: 500;
        border-radius: 12px;
        border: none;
        background-color: #e0e0e0;
        color: #333;
    }
    .stButton > button:hover {
        background-color: #d0d0d0;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 6px;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

if "display" not in st.session_state:
    st.session_state.display = "0"
if "angka1" not in st.session_state:
    st.session_state.angka1 = None
if "operasi" not in st.session_state:
    st.session_state.operasi = None
if "reset" not in st.session_state:
    st.session_state.reset = False

def tekan_angka(num):
    if st.session_state.reset:
        st.session_state.display = str(num)
        st.session_state.reset = False
    elif st.session_state.display == "0":
        st.session_state.display = str(num)
    else:
        st.session_state.display += str(num)

def tekan_operasi(op):
    st.session_state.angka1 = float(st.session_state.display)
    st.session_state.operasi = op
    st.session_state.reset = True

def hitung():
    if st.session_state.angka1 is not None and st.session_state.operasi:
        angka2 = float(st.session_state.display)
        if st.session_state.operasi == "+":
            hasil = st.session_state.angka1 + angka2
        elif st.session_state.operasi == "-":
            hasil = st.session_state.angka1 - angka2
        elif st.session_state.operasi == "x":
            hasil = st.session_state.angka1 * angka2
        elif st.session_state.operasi == "/":
            if angka2 != 0:
                hasil = st.session_state.angka1 / angka2
            else:
                st.session_state.display = "Error"
                return
        
        if hasil == int(hasil):
            st.session_state.display = str(int(hasil))
        else:
            st.session_state.display = str(round(hasil, 8))
        
        st.session_state.angka1 = None
        st.session_state.operasi = None
        st.session_state.reset = True

def clear():
    st.session_state.display = "0"
    st.session_state.angka1 = None
    st.session_state.operasi = None

st.markdown(f"""
<div style="background: #f5f5f5; padding: 20px 15px; font-size: 40px; 
    text-align: right; border-radius: 12px; margin-bottom: 15px; 
    font-family: -apple-system, sans-serif; color: #222;">
    {st.session_state.display}
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("C"): clear()
with c2:
    if st.button("/"): tekan_operasi("/")
with c3:
    if st.button("x"): tekan_operasi("x")
with c4:
    if st.button("-"): tekan_operasi("-")

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("7"): tekan_angka(7)
with c2:
    if st.button("8"): tekan_angka(8)
with c3:
    if st.button("9"): tekan_angka(9)
with c4:
    if st.button("+"): tekan_operasi("+")

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("4"): tekan_angka(4)
with c2:
    if st.button("5"): tekan_angka(5)
with c3:
    if st.button("6"): tekan_angka(6)
with c4:
    if st.button("="): hitung()

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("1"): tekan_angka(1)
with c2:
    if st.button("2"): tekan_angka(2)
with c3:
    if st.button("3"): tekan_angka(3)
with c4:
    if st.button("."): 
        if "." not in st.session_state.display:
            st.session_state.display += "."

c1, c2 = st.columns([2, 2])
with c1:
    if st.button("0"): tekan_angka(0)
