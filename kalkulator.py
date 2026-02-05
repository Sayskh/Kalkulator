import streamlit as st

st.set_page_config(page_title="Kalkulator", layout="centered")

st.markdown("""
<style>
    .stApp {
        background-color: #0a0a0a;
    }
    .block-container {
        max-width: 360px;
        padding-top: 2rem;
    }
    .stButton > button {
        width: 72px;
        height: 72px;
        font-size: 24px;
        font-weight: 400;
        border-radius: 50%;
        border: none;
        background-color: #3d4a3a;
        color: #fff;
        margin: 0 auto;
        display: block;
    }
    .stButton > button:hover {
        opacity: 0.8;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 12px;
        margin-bottom: 12px;
        justify-content: center;
    }
    
    /* Operator column - teal green */
    div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"]:last-child button {
        background-color: #1a8a6e !important;
    }
</style>
""", unsafe_allow_html=True)

if "display" not in st.session_state:
    st.session_state.display = ""

def tekan(val):
    st.session_state.display += str(val)

def kurung():
    buka = st.session_state.display.count("(")
    tutup = st.session_state.display.count(")")
    if buka > tutup:
        st.session_state.display += ")"
    else:
        st.session_state.display += "("

def clear():
    st.session_state.display = ""

def hapus():
    if st.session_state.display:
        st.session_state.display = st.session_state.display[:-1]

def persen():
    try:
        hasil = eval(st.session_state.display.replace("x", "*")) / 100
        st.session_state.display = str(hasil)
    except:
        pass

def hitung():
    try:
        ekspresi = st.session_state.display.replace("x", "*")
        hasil = eval(ekspresi)
        if isinstance(hasil, float) and hasil == int(hasil):
            st.session_state.display = str(int(hasil))
        else:
            st.session_state.display = str(round(hasil, 8))
    except:
        st.session_state.display = "Error"

tampilan = st.session_state.display if st.session_state.display else "0"

st.markdown(f"""
<div style="background: #1a1a1a; color: #1a8a6e; padding: 25px 20px; 
    font-size: 42px; text-align: right; border-radius: 15px; 
    margin-bottom: 20px; font-family: monospace; min-height: 45px;
    border: 1px solid #2a2a2a;">
    {tampilan}
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("C", on_click=clear)
with c2:
    st.button("( )", on_click=kurung)
with c3:
    st.button("%", on_click=persen)
with c4:
    st.button("÷", on_click=tekan, args=["/"])

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("7", on_click=tekan, args=["7"])
with c2:
    st.button("8", on_click=tekan, args=["8"])
with c3:
    st.button("9", on_click=tekan, args=["9"])
with c4:
    st.button("×", on_click=tekan, args=["x"])

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("4", on_click=tekan, args=["4"])
with c2:
    st.button("5", on_click=tekan, args=["5"])
with c3:
    st.button("6", on_click=tekan, args=["6"])
with c4:
    st.button("−", on_click=tekan, args=["-"])

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("1", on_click=tekan, args=["1"])
with c2:
    st.button("2", on_click=tekan, args=["2"])
with c3:
    st.button("3", on_click=tekan, args=["3"])
with c4:
    st.button("＋", on_click=tekan, args=["+"])

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("⌫", on_click=hapus)
with c2:
    st.button("0", on_click=tekan, args=["0"])
with c3:
    st.button(".", on_click=tekan, args=["."])
with c4:
    st.button("=", on_click=hitung)
