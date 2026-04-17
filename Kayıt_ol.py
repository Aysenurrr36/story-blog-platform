import streamlit as st
from datetime import date
from hikaye_olustur import kullanici_ekleme

st.title("Kayıt Ol") 

kullanici_adi = st.text_input("Kullanıcı Adı")
email = st.text_input("Email")
sifre = st.text_input("Şifre", type="password")
dogum_tarihi = st.date_input("Doğum Tarihi", date(2000, 1, 1))
cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])

if st.button("Kayıt Ol"):
    st.success(kullanici_ekleme(kullanici_adi, email, sifre, dogum_tarihi, cinsiyet))  
   
    
    
