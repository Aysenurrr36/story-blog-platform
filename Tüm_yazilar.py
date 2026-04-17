import streamlit as st
from hikaye_olustur import tüm_yazilari_görüntüleme

# Sayfa başlığı ve açıklama
st.title("Kullanıcılar ve Yazıları")
st.write("---")
st.write(" İstediğniz seçeneğe göre yazıları görüntüleyebilirsiniz.")


hikaye_listesi=tüm_yazilari_görüntüleme()


kategoriler=set()
diller=set()  



for hikayeler in hikaye_listesi.values(): 
    for hikaye in hikayeler:
        kategoriler.add(hikaye["kategori"]) 
        diller.add(hikaye["dil"])  



# Kategori ve dil seçime
secilen_kategori=st.selectbox("Bir kategori seçin:", ["Tüm Kategoriler"] + list(kategoriler))
secilen_dil=st.selectbox("Bir dil seçin:", ["Tüm Diller"] + list(diller))


st.write("---")

# Filtrelenmiş yazıları listeleme
st.header("Yazılar")
filtrelenmis_yazilar={} 

# Eğer kategori ve dil seçildiyse yazıları filtrele
for kullanici, hikayeler in hikaye_listesi.items(): 
        if secilen_kategori != "Tüm Kategoriler" and hikaye["kategori"] != secilen_kategori:
            continue 
        if secilen_dil != "Tüm Diller" and hikaye["dil"] != secilen_dil:
            continue
        if kullanici not in filtrelenmis_yazilar: 
            filtrelenmis_yazilar[kullanici]=[]
        filtrelenmis_yazilar[kullanici].append(hikaye) 
# Filtrelenmiş yazıya ait bilgiler
if filtrelenmis_yazilar:
    for kullanici, hikayeler in filtrelenmis_yazilar.items(): 
        st.write("---")
        st.subheader(f"Kullanıcı: {kullanici}") 
        for hikaye in hikayeler: 
            st.markdown(f'<h4 style="color:red;">{hikaye["baslik"]}</h4>', unsafe_allow_html=True) 
            st.write(f"Kategori: {hikaye['kategori']}")
            st.write(f"Yayınlanma Tarihi: {hikaye['yayin_tarihi']}")
            st.write(f"Anahtar Kelimeler: {hikaye['anahtar_kelimeler']}")
            st.write(hikaye['icerik'])
            
else:
    st.warning("Seçilen filtreye  göre yazı bulunamadı.")
