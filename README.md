# 🛡️ Kurumsal Siber Güvenlik & Bellek Optimizasyonu: Bloom Filter Simülasyonu

Bu proje; yüksek trafikli siber güvenlik, antivirüs (EDR) ve web ağ altyapılarında (WAF/CDN) karşılaşılan **Disk I/O darboğazlarını ve veritabanı maliyetlerini %99 oranında azaltan**, Python tabanlı modüler bir olasılıksal veri yapısı (Bloom Filter) simülasyonudur.

---

## 📖 Mimari Hikaye ve Problem

Dehşet verici büyüklükteki veri setlerini (milyonlarca zararlı imza, URL kara listesi veya metin arşivi) klasik veritabanlarında (`PostgreSQL`, `Redis` vb.) sorgulamak, sistemlerde ciddi gecikmelere (Network Latency) ve disk darboğazlarına yol açar. Tamamen bellekte (RAM) tutmak ise gigabaytlarca maliyet yaratır.

**Çözüm:** Bu projede geliştirilen **Bloom Filter** mimarisi sayesinde, milyonlarca kayıt megabaytlar seviyesindeki bit dizilerine sıkıştırılır:
1. **Kesinlikle Yok (False):** Sorgulanan veri filtrede yoksa, yavaş veritabanına **hiç uğramadan** anında reddedilir (%100 doğruluk).
2. **Muhtemelen Var (True):** Veri filtrede görünüyorsa, çok küçük bir olasılıksal hata payıyla (`p`) sadece şüpheli kayıtlar derin analiz için ana veritabanına gönderilir.

---

## 🚀 Gerçek Dünya Senaryoları & Kullanım Alanları

Proje arayüzünde canlı olarak test edebileceğiniz 4 temel kurumsal senaryo bulunmaktadır:

1. **🦠 Malware Tespiti (EDR / Antivirüs):** 
   Milyonlarca zararlı dosya SHA-256 hash imzasını istemci RAM'inde çok küçük bir alanda tutarak, buluta veya diske sormadan anında güvenli/zararlı filtrelemesi yapar.
2. **🌐 Web & WAF Güvenliği (Edge Katmanı):** 
   CDN ve Edge sunucularında bilinen zararlı URI, SQL Injection kalıplarını ve IP'leri milisaniyeler içinde ön filtrelemeden geçirir.
3. **🌐 URL / Phishing Koruması:** 
   Tarayıcıların zararlı web sitelerini anlık olarak engellemek için kullandığı kara liste mantığını simüle eder.
4. **📚 Büyük Metin Arşivleri:** 
   Milyonlarca kelimelik arşivlerde disk okuma maliyetini sıfıra indirerek kelime arama optimizasyonu sağlar.

---

## ⚙️ Matematiksel Altyapı ve Formüller

Filtre, kapasite ($n$) ve hedeflenen hata payı ($p$) değerlerine göre en optimum bellek boyutunu ($m$) ve hash fonksiyonu sayısını ($k$) dinamik olarak hesaplar:

- **Bit Boyutu ($m$):** $$m = -\frac{n \cdot \ln(p)}{(\ln(2))^2}$$
- **Optimum Hash Sayısı ($k$):** $$k = \frac{m}{n} \cdot \ln(2)$$

---

## 💻 Kurulum ve Çalıştırma

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Repoyu Klonlayın:**
   ```bash
   git clone <repo-url>
   cd bloom-filter-project


   Gerekli Kütüphaneleri Yükleyin:

Bash
pip install streamlit
Streamlit Arayüzünü Başlatın:

Bash
streamlit run app.py
Tarayıcınızda açılan http://localhost:8501 adresinden interaktif paneli test edebilirsiniz.

🛠️ Teknolojiler
Python (Modüler Sınıf Mimarisi)

MurmurHash3 / Özelleştirilmiş Hash Fonksiyonları

Streamlit (İnteraktif Web Arayüzü & İstatistik Paneli)