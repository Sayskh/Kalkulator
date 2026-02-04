import streamlit as st

st.set_page_config(page_title="Kalkulator", layout="centered")

st.markdown("""
<style>
    .main {
        max-width: 400px;
        margin: 0 auto;
    }
    .stButton > button {
        width: 100%;
        height: 70px;
        font-size: 28px;
        font-weight: bold;
        border-radius: 15px;
        border: none;
        background-color: #333;
        color: white;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background-color: #555;
        transform: scale(1.02);
    }
    .stButton > button:active {
        background-color: #666;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 8px;
        margin-bottom: 8px;
    }
    .display-box {
        background: linear-gradient(145deg, #1a1a2e, #16213e);
        color: #00ff88;
        padding: 25px;
        font-size: 42px;
        text-align: right;
        border-radius: 20px;
        margin-bottom: 20px;
        font-family: 'Courier New', monospace;
        box-shadow: inset 0 4px 8px rgba(0,0,0,0.4);
        min-height: 50px;
        word-wrap: break-word;
    }
    .calc-container {
        background: linear-gradient(145deg, #2d2d44, #1f1f2e);
        padding: 25px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    h1 {
        text-align: center;
        color: #fff;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Kalkulator</h1>", unsafe_allow_html=True)

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
    st.session_state.reset = False

st.markdown('<div class="calc-container">', unsafe_allow_html=True)

st.markdown(f'<div class="display-box">{st.session_state.display}</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("C", key="clear"): clear()
with c2:
    if st.button("/", key="div"): tekan_operasi("/")
with c3:
    if st.button("x", key="mul"): tekan_operasi("x")
with c4:
    if st.button("-", key="sub"): tekan_operasi("-")

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("7", key="7"): tekan_angka(7)
with c2:
    if st.button("8", key="8"): tekan_angka(8)
with c3:
    if st.button("9", key="9"): tekan_angka(9)
with c4:
    if st.button("+", key="add"): tekan_operasi("+")

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("4", key="4"): tekan_angka(4)
with c2:
    if st.button("5", key="5"): tekan_angka(5)
with c3:
    if st.button("6", key="6"): tekan_angka(6)
with c4:
    if st.button("=", key="eq"): hitung()

c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("1", key="1"): tekan_angka(1)
with c2:
    if st.button("2", key="2"): tekan_angka(2)
with c3:
    if st.button("3", key="3"): tekan_angka(3)
with c4:
    if st.button(".", key="dot"): 
        if "." not in st.session_state.display:
            st.session_state.display += "."

c1, c2 = st.columns([2, 2])
with c1:
    if st.button("0", key="0"): tekan_angka(0)

st.markdown('</div>', unsafe_allow_html=True)
