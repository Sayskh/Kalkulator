import streamlit as st

st.set_page_config(page_title="Kalkulator", layout="centered")

st.title("Kalkulator Sederhana")

angka1 = st.number_input("Masukkan angka pertama", value=0, step=1, format="%d")
angka2 = st.number_input("Masukkan angka kedua", value=0, step=1, format="%d")

operasi = st.selectbox("Pilih operasi", ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

if st.button("Hitung"):
    if operasi == "Penjumlahan":
        hasil = angka1 + angka2
    elif operasi == "Pengurangan":
        hasil = angka1 - angka2
    elif operasi == "Perkalian":
        hasil = angka1 * angka2
    elif operasi == "Pembagian":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            st.error("Tidak bisa membagi dengan nol")
            hasil = None
    
    if hasil is not None:
        st.success(f"Hasil: {hasil}")