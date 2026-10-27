# 🛡️ OmniFilter Enterprise Suite: Multi-Layered Memory & Security Optimization

> High-performance enterprise security and RAG acceleration system powered by probabilistic Bloom Filter architecture.

---

## 🚀 Proje Hakkında (About)
**OmniFilter Enterprise Suite**, büyük ölçekli kurumsal sistemlerde bellek optimizasyonu, gerçek zamanlı zararlı tespiti (EDR), web güvenliği (WAF) ve yapay zeka (RAG) indeksleme süreçlerini milisaniyelik hızlara indiren **hafıza-verimli** bir mimaridir. 

Geleneksel veri tabanlarının ve ağır algoritmaların yarattığı CPU/RAM darboğazını, **Bloom Filter** veri yapısının matematiksel gücünü kullanarak ortadan kaldırır.

---

## 🏗️ Sistem Mimarisi ve Modüller

Proje, 7/24 arka planda çalışan otonom ajanlar (**daemons**) ve görsel bir yönetim panelinden oluşur:

1. **`edr_daemon.py` (Malware & EDR Ajanı):**
   * `./test_downloads` dizinini 7/24 izler.
   * Yeni düşen dosyaların SHA-256 imzasını hesaplar.
   * Bloom Filter belleği üzerinden milisaniyeler içinde zararlı/karantina kontrolü yapar ve tehditleri otomatik tecrit eder.

2. **`waf_proxy.py` (Edge WAF Ağ Geçidi):**
   * Gelen ağ isteklerini ve web saldırı kalıplarını (SQL Injection, XSS) simüle ederek süzer.
   * Bilinen tehditleri HTTP 403 ile anında engeller.

3. **`archive_sync.py` (RAG & Metin Arşivi Senkronizatörü):**
   * `./archive_folder` dizinini izleyerek eklenen belgeleri tokenize eder.
   * Yapay zeka (LLM) arama motorları için kelime tabanını anında belleğe indeksler, gereksiz yükü önler.

4. **`app.py` (Streamlit Kurumsal Kontrol Paneli):**
   * Sistem yöneticileri için canlı gözlem, imza yönetimi ve performans metrikleri sunan görsel arayüz.

---

## 📊 Performans Avantajları
* **Ultra Düşük Gecikme:** Aramalar ve imza sorguları $O(k)$ karmaşıklığı sayesinde $0.01\text{ ms}$ civarında gerçekleşir.
* **Sıfır Yanlış Negatif (Zero False Negatives):** Bir öğe filtrede yoksa kesinlikle yoktur garantisi sunar.
* **Düşük Bellek Tüketimi:** Milyonlarca imza ve kelime, gigabaytlarca RAM harcamadan sıkıştırılmış bit dizilerinde saklanır.

---

## 🛠️ Kurulum ve Çalıştırma

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/neslihan6116/bloom-filter-enterprise.git](https://github.com/neslihan6116/bloom-filter-enterprise.git)
   cd bloom-filter-enterprise

1. Gerekli Kütüphaneleri Yükleyin:
pip install -r requirements.txt

2. Görsel Panoyu Başlatın:
streamlit run app.py

3. Arka Plan Ajanlarını Çalıştırın (Ayrı Terminallerde):
python edr_daemon.py
python waf_proxy.py
python archive_sync.py

🎯 Kullanım Senaryoları
1. Siber Güvenlik Şirketleri & EDR: Uç nokta zararlı yazılım tespiti ve karantina.

2. E-Ticaret & Finans: Edge seviyesinde hızlı WAF ve saldırı engelleme.

3. Kurumsal RAG & Yapay Zeka: Devasa doküman arşivlerinde hızlı veri eleme ve arama optimizasyonu.

