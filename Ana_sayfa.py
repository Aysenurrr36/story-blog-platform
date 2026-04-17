
import streamlit as st


st.set_page_config(page_title="Kendini Yaz", page_icon="📚", layout="wide") # Sayfanın başlık,simge ve düzenini ayralama
st.title("Hoş Geldiniz!")
st.balloons()

st.markdown("**Bu sitede hikaye ya da blog yazabilir , yazılarınızı düzenleyebilirsiniz.**")
st.markdown("**Kaydolmadan veya giriş yapmadan da paylaşılan yazıları görebilirsiniz.**")
st.markdown("Aşağıdaki butona tıklayarak yazıları görebilirsiniz! 👇🏻")
st.page_link("sayfalar/Tüm_yazilar.py", label="Yayınlar", icon=":material/apps:")
