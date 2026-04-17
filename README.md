# Story Blog Platform

Bu proje, kullanıcıların kendi hikayelerini yazabildiği veya günlük hayatta yaptıkları deneyimleri paylaşabildiği bir web uygulamasıdır.  
Uygulama Python dili kullanılarak geliştirilmiş olup, veritabanı yönetimi için MySQL tercih edilmiştir.

---

##  Proje Özellikleri

- Kullanıcı kayıt ve giriş sistemi
- Hikaye oluşturma ve paylaşma
- Hikaye düzenleme ve silme
- Kategorilere göre hikaye listeleme
- Kullanıcıya özel içerik görüntüleme

---

##  Kullanıcı Bilgileri

Sistemde her kullanıcı için aşağıdaki bilgiler tutulur:

- Kullanıcı Adı
- E-posta Adresi
- Şifre
- Doğum Tarihi
- Cinsiyet

---

## Hikaye Bilgileri

Her hikaye için aşağıdaki veriler saklanır:

- Başlık
- İçerik
- Yayınlama Tarihi
- Kategori (örneğin: kişisel, seyahat, yemek)
- Anahtar Kelimeler
- Dil
- Uzunluk

---

## Temel İşlemler

### Ekleme İşlemleri
- Yeni kullanıcı kaydı oluşturma
- Yeni hikaye ekleme

### Silme İşlemleri
- Hikaye silme
- Kullanıcı hesabı silme

###  Güncelleme İşlemleri
- Hikaye başlığı, içeriği ve dili güncelleme
- Kullanıcı bilgilerini güncelleme

### Listeleme İşlemleri
- Tüm hikayeleri listeleme
- Belirli bir kullanıcıya ait hikayeleri görüntüleme
- Kategoriye göre hikaye listeleme
- Kullanıcı bilgilerini görüntüleme

---

## Kullanılan Teknolojiler

| Teknoloji | Açıklama | Versiyon |
|----------|--------|---------|
| Python | Backend geliştirme | 3.11.0 |
| Streamlit | Web uygulama arayüzü | 1.41.1 |
| MySQL | Veritabanı yönetimi | 8.0.36 |
| mysql-connector-python | Veritabanı bağlantısı | 9.1.0 |
| Visual Studio Code | Geliştirme ortamı | 1.96.2 |

---

##  Kurulum

Projeyi çalıştırmak için:

```bash
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi
pip install -r requirements.txt
streamlit run app.py
```

---

## Notlar

- Veritabanı bağlantı ayarlarını kendi MySQL yapılandırmanıza göre düzenlemeniz gerekmektedir.
- Proje geliştirme ve öğrenme amaçlıdır.

## Gelecek Geliştirmeler

- Kullanıcı giriş sistemi geliştirme (authentication)
- Yorum ve beğeni sistemi ekleme
- Mobil uyumlu arayüz
- API desteği


