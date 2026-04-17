import streamlit as st
from hikaye_olustur import hikaye_ekleme
from datetime import date


if "kullanici_id" not in st.session_state:
    st.warning("Yazı eklemek için önce giriş yapmalısınız!") 
    st.stop()


# Sayfa başlığı
st.title("Hikaye veya Blog Ekle")


baslik = st.text_input("Başlık")
icerik = st.text_area("İçerik")
yayin_tarihi = st.date_input("Yayın Tarihi", value=date.today())
kategori = st.text_input("Kategori")
anahtar_kelimeler = st.text_input("Anahtar Kelimeler")
dil = st.selectbox("Dil", ["Türkçe", "İngilizce"])

# Hikaye uzunluğu
uzunluk = len(icerik.strip())  

# Hikaye kaydetme 
if st.button("Kaydet"): 
    if baslik.strip() == "" or icerik.strip() == "":
        st.error("Başlık ve içerik alanları boş bırakılamaz.")
    else: 
        st.success(hikaye_ekleme(
            st.session_state["kullanici_id"],
            baslik,
            icerik,
            yayin_tarihi,
            kategori,
            anahtar_kelimeler,
            dil,
            uzunluk) )
        st.balloons()  