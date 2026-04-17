# -*- coding: utf-8 -*-

from datetime import date
from mysql.connector import connection


#Bu veritabanına bağlanmak için oluşturulan fonksiyon
def veritabanina_baglanma():
       return connection.MySQLConnection(user='root', password='3636',
 host='127.0.0.1',   database='hikaye_olustur')


#Bu veritabanına kullanıcı eklemek için oluşturulan fonksiyon
def kullanici_ekleme(                                    
        kullanici_adi,       
        email,                                
        sifre,                              
        dogum_tarihi,
        cinsiyet
):
    cnx=veritabanina_baglanma()               
    cursor=cnx.cursor()                       

    if kullanici_adi and email and sifre:     

        ekle_kullanici=""" 
        INSERT INTO  kullanici_bilgileri(kullanici_adi,email,sifre,dogum_tarihi,cinsiyet)
        VALUES(%s,%s,%s,%s,%s)
        """ 

        cursor.execute(ekle_kullanici,(kullanici_adi,email,sifre,dogum_tarihi,cinsiyet))   
        cnx.commit()               
        cursor.close()             
        cnx.close()

        return "Kullanıcı eklenmiştir."   
    
    else:                                
        cursor.close()
        cnx.close()
        return "Zorunlu alanları boş bırakmayınız."

#Bu veritabanına hikaye ekleme için oluşturulan fonksiyon
def hikaye_ekleme(
        kullanici_id,            
        baslik,
        icerik,
        yayin_tarihi,                           
        kategori,
        anahtar_kelimeler,
        dil,
        uzunluk
):  
    cnx=veritabanina_baglanma()
    cursor=cnx.cursor()

    if kullanici_id and baslik and icerik:

        yayin_tarihi=yayin_tarihi or date.today()  
        uzunluk=len(icerik) 
        ekle_hikaye= """
        INSERT INTO hikaye_bilgileri(kullanici_id,baslik,icerik,yayin_tarihi,kategori,anahtar_kelimeler,dil,uzunluk)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """ 
        cursor.execute(ekle_hikaye,(kullanici_id,baslik,icerik,yayin_tarihi,kategori,anahtar_kelimeler,dil,uzunluk))
        cnx.commit()
        cursor.close()
        cnx.close()

        return "Yazı eklenmiştir."
    
    else:
        cursor.close()
        cnx.close()
        return "Zorunlu alanları boş bırakmayınız."

#Kullanıcı bilgilerini güncellemek için oluşturulan fonksiyon   
def kullanici_güncelleme(
    kullanici_id,
    yeni_kullanici_adi=None, 
    yeni_email=None,
    yeni_sifre=None
):
    cnx = veritabanina_baglanma()
    cursor = cnx.cursor()

    
    güncelle = """
        UPDATE kullanici_bilgileri
        SET kullanici_adi = %s, email = %s, sifre = %s
        WHERE id = %s
    """

    
    cursor.execute("SELECT kullanici_adi, email, sifre FROM kullanici_bilgileri WHERE id = %s", (kullanici_id,))
    gecmis_bilgi = cursor.fetchone()  

    if not gecmis_bilgi: 
        cursor.close()
        cnx.close()
        return "Kullanıcı bulunamadı."

    
    kullanici_adi_yeni = yeni_kullanici_adi if yeni_kullanici_adi else gecmis_bilgi[0]
    email_yeni = yeni_email if yeni_email else gecmis_bilgi[1]
    sifre_yeni = yeni_sifre if yeni_sifre else gecmis_bilgi[2]

    
    cursor.execute(güncelle, (kullanici_adi_yeni, email_yeni, sifre_yeni, kullanici_id))
    cnx.commit()

    cursor.close()
    cnx.close()

    return "Kullanıcı bilgileri güncellendi."

#Hikaye bilgilerini güncellemek için oluşturulan fonksiyon
def hikaye_güncelleme(
        hikaye_id,
        yeni_baslik= None,   
        yeni_icerik= None
        
): 
        cnx=veritabanina_baglanma()
        cursor=cnx.cursor()
        if not yeni_baslik or not yeni_icerik:
            cursor.close()
            cnx.close()
            return "Güncellenecek bilgi bulunamadı. "

       
        cursor.execute("SELECT baslik,icerik FROM hikaye_bilgileri WHERE id =%s",(hikaye_id,))   
        gecmis_bilgi= cursor.fetchone()

        if not gecmis_bilgi:
            cursor.close()
            cnx.close()
            return "Hikaye bulunamadı." 
        
        baslik_yeni= yeni_baslik if yeni_baslik else gecmis_bilgi[0]
        icerik_yeni= yeni_icerik if yeni_icerik else gecmis_bilgi[1]

        yeni_uzunluk=len(yeni_icerik) if yeni_icerik else len(gecmis_bilgi[1]) 

        güncelle = """
        UPDATE hikaye_bilgileri
        SET baslik = %s, icerik = %s, uzunluk = %s
        WHERE id = %s
        """

        cursor.execute(güncelle,(baslik_yeni,icerik_yeni,yeni_uzunluk,hikaye_id))

        cnx.commit()
        cursor.close()
        cnx.close()

        return "Hikaye bilgileri güncellendi."
        
#Kullanıcyı ve yazılarını veritabanından silmek için oluşturulan fonksiyon
def silme(kullanici_id=None): 
    cnx = veritabanina_baglanma()
    cursor = cnx.cursor()

    if kullanici_id:
        
        sil_hikaye = "DELETE FROM hikaye_bilgileri WHERE kullanici_id = %s"
        cursor.execute(sil_hikaye, (kullanici_id,))  
        sil_kullanici = "DELETE FROM kullanici_bilgileri WHERE id = %s"
        cursor.execute(sil_kullanici, (kullanici_id,))  
        cnx.commit()
        cursor.close()
        cnx.close()

        return "Kullanıcı ve hikayeleri silinmiştir."
    else:
        cursor.close()
        cnx.close()
        return "Kullanıcı ID'si geçersiz."
    
#Sadece kullanıcın yazısını silmek için oluşturulan fonksiyon   
def hikaye_silme(hikaye_id):
    cnx = veritabanina_baglanma()
    cursor = cnx.cursor()

    # Hikayeyi silme
    sil_hikaye = "DELETE FROM hikaye_bilgileri WHERE id = %s"
    cursor.execute(sil_hikaye, (hikaye_id,))  
    cnx.commit()
    cursor.close()
    cnx.close()

    return f"Hikaye {hikaye_id} başarıyla silindi."

#Kullanıcıyı ve yazılarını görüntülemek için oluşturulan fonksiyon (hesap bilgilerinde görüntülemek için)
def kullanici_ve_hikaye_listeleme(kullanici_id):

    cnx=veritabanina_baglanma()
    cursor=cnx.cursor()
    
    cursor.execute("SELECT * FROM kullanici_bilgileri WHERE id = %s", (kullanici_id,))
    kullanici_bilgileri = cursor.fetchone()
    

    
    cursor.execute("SELECT * FROM hikaye_bilgileri WHERE kullanici_id = %s", (kullanici_id,))
    hikayeler = cursor.fetchall()

    cursor.close()
    cnx.close()

    return kullanici_bilgileri,hikayeler

#Kullanıcı giriş yaparken bu fonksiyon çağrılır
def kullanici_girisi(kullanici_adi,email,sifre): 
   
   cnx=veritabanina_baglanma()
   cursor=cnx.cursor()
   cursor.execute("SELECT id FROM kullanici_bilgileri WHERE kullanici_adi=%s AND email=%s AND sifre =%s ",(kullanici_adi,email,sifre)) 
   kullanici=cursor.fetchone()

   if kullanici: 
       return kullanici[0]     
   else:
       return  None  

#Kullanıcıların tüm yazılarını görmek için oluşturulan fonksiyon (herkes tarafından)
def tüm_yazilari_görüntüleme(): 

    cnx=veritabanina_baglanma()
    cursor=cnx.cursor()

    görüntüle = """
    SELECT  kullanici_bilgileri.kullanici_adi,
            hikaye_bilgileri.baslik,
            hikaye_bilgileri.icerik,
            hikaye_bilgileri.kategori,
            hikaye_bilgileri.yayin_tarihi,
            hikaye_bilgileri.anahtar_kelimeler,
            hikaye_bilgileri.dil
    FROM hikaye_bilgileri  
    INNER JOIN kullanici_bilgileri 
    ON hikaye_bilgileri.kullanici_id = kullanici_bilgileri.id
    """ 
    cursor.execute(görüntüle)
    bilgiler = cursor.fetchall() 

    
    cursor.close()
    cnx.close()

    # Hikaye listesini oluşturma
    hikaye_listesi = {} 
    for kullanici, baslik, icerik, kategori, yayin_tarihi, anahtar_kelimeler, dil in bilgiler: 
        if kullanici not in hikaye_listesi: 
            hikaye_listesi[kullanici] = []
        hikaye_listesi[kullanici].append({   
            "baslik": baslik,
            "icerik": icerik,
            "kategori": kategori,
            "yayin_tarihi": yayin_tarihi,
            "anahtar_kelimeler": anahtar_kelimeler,
            "dil": dil  
        })

    return hikaye_listesi 