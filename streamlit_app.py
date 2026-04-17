import streamlit as st

# Sitedeki sayfaları oluşturma

ana_sayfa= st.Page(
    page="sayfalar/Ana_sayfa.py",
    title="Hikaye veya Blog Oluşturma Sitesi",
    icon=":material/home:",
    
    
)

giris_yap=st.Page(
    page="sayfalar/Giriş_yap.py",
    title="Giriş Yap",
    icon=":material/login:",
)


kayit_ol=st.Page(
    page="sayfalar/Kayıt_ol.py",
    title="Kayıt Ol",
    icon=":material/how_to_reg:",
)

hikaye_yaz=st.Page(
    page="sayfalar/Hikaye_yaz.py",
    title="Hikaye veya Blog ekle",
    icon=":material/text_snippet:"

)

hesap=st.Page(
    page="sayfalar/Hesap_bilgileri.py",
    title="Hesabım",
    icon=":material/person:",
)


yazilar=st.Page(
    page="sayfalar/Tüm_yazilar.py",
    title="Yayınlar",
    icon=":material/apps:",
)


sf= st.navigation(
    {
        "Ana Sayfa":[ana_sayfa],
        "Giriş yap veya Hesap Oluştur": [giris_yap,kayit_ol],
        "Yazmaya Başla":[hikaye_yaz],
        "Yönet":[hesap],
        "Akış":[yazilar]
    
    }

)


       
sf.run()  
    


