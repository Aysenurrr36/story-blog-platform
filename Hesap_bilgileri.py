import streamlit as st
from hikaye_olustur import (
    kullanici_ve_hikaye_listeleme,
    hikaye_güncelleme,
    silme,
    kullanici_güncelleme,
    hikaye_silme
)

if "kullanici_id" not in st.session_state:
    st.warning("Lütfen önce giriş yapınız!")  
    st.stop()

st.title("Hesap") 


kullanici_bilgileri, hikayeler = kullanici_ve_hikaye_listeleme(st.session_state["kullanici_id"])

# Kullanıcı bilgileri
st.subheader("Kullanıcı Bilgilerim")
st.write(f"**Kullanıcı Adı:** {kullanici_bilgileri[1]}")
st.write(f"**Email:** {kullanici_bilgileri[2]}")
st.write(f"**Cinsiyet:** {kullanici_bilgileri[5]}")
st.write(f"**Doğum Tarihi:** {kullanici_bilgileri[4]}")
st.write("---")

# Kullanıcı bilgileri güncelleme 
st.subheader("Kullanıcı Bilgilerimi Güncelle")
yeni_kullanici_adi = st.text_input("Yeni Kullanıcı Adı")
yeni_email = st.text_input("Yeni Email")
yeni_sifre = st.text_input("Yeni Şifre", type="password")

if st.button("Güncelle"):
    if yeni_kullanici_adi and yeni_email and yeni_sifre: 
        st.success(kullanici_güncelleme(
            st.session_state["kullanici_id"],
            yeni_kullanici_adi=yeni_kullanici_adi,
            yeni_email=yeni_email,
            yeni_sifre=yeni_sifre
        ))
        st.rerun() 
        
    else:
        st.warning("Kullanıcı adı, email ve şifre boş olamaz.")

if st.button("Hesabı Sil"): 
        st.success(silme(kullanici_id=st.session_state["kullanici_id"]))
        st.session_state.clear()  
        st.rerun()  
        

st.write("---")


# Yazılar
st.subheader("Yazılarım")

if hikayeler: 
    for hikaye in hikayeler:
        with st.expander(hikaye[2]): 
            st.write(f"**Kategori:** {hikaye[5]}")
            st.write(f"**İçerik:** {hikaye[3]}")
            
            
            yeni_baslik = st.text_input("Yeni Başlık", key=f"baslik_{hikaye[0]}")
            yeni_icerik = st.text_area("Yeni İçerik",  key=f"icerik_{hikaye[0]}")
            
            if st.button(f"Güncellemeyi Kaydet", key=f"kaydet_{hikaye[0]}"):
                if yeni_baslik and yeni_icerik:
                    st.success( hikaye_güncelleme(hikaye[0], yeni_baslik, yeni_icerik))
                    st.rerun() 
                else:
                    st.warning("Başlık ve içerik boş olamaz.")

            # Hikaye Silme
            if st.button(f"Sil", key=f"sil_{hikaye[0]}"):
                st.success(hikaye_silme(hikaye[0]))
                st.rerun()  
        




if st.button("Çıkış Yap"):
    st.session_state.clear()  
    st.rerun()  