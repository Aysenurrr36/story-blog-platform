import streamlit as st
from hikaye_olustur import kullanici_girisi
import pandas as pd

# Sayfa başlığı
st.title("Kullanıcı Girişi")

kullanici_adi=st.text_input("Kullanıcı Adı")
email = st.text_input("Email")
sifre = st.text_input("Şifre", type="password")
if st.button("Giriş Yap"):
  kullanici = kullanici_girisi(kullanici_adi,email,sifre) 
  if kullanici:
        st.session_state["kullanici_id"] = kullanici
        st.success("Başarıyla giriş yapıldı!")
    
  else:
        st.error("Geçersiz kullanıcı adı veya şifre.")



st.write("Hesabınız yok mu ? Hemen kaydolun.")
st.page_link("sayfalar/Kayıt_ol.py", label="Kayıt Ol", icon=":material/how_to_reg:")

