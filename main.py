from bloom_filter.filter import BloomFilter

def main():
    print("=" * 60)
    print("PROJE 1: Dağıtık Dağılım ve Üyelik Filtresi (Bloom Filter) Senaryoları")
    print("=" * 60)
    
    # -------------------------------------------------------------------------
    # SENARYO 1: Kötü Amaçlı Web Siteleri / URL Kara Listesi (Phishing Koruması)
    # -------------------------------------------------------------------------
    print("\n--- SENARYO 1: Kötü Amaçlı URL Kara Listesi Kontrolü ---")
    
    # Karakteristikler: Yüksek kapasite, çok düşük hata payı (%0.1)
    url_capacity = 5000
    url_error_rate = 0.001
    
    phishing_filter = BloomFilter(capacity=url_capacity, error_rate=url_error_rate)
    
    # Bilinen zararlı (phishing) web siteleri kara listeye ekleniyor
    zararli_siteler = [
        "phishing-ornek-site1.com",
        "sahte-banka-giris.net",
        "bedava-hediye-kazan.org",
        "guvenli-olmayan-site.com"
    ]
    
    for site in zararli_siteler:
        phishing_filter.add(site)
        print(f"[KARA LİSTE EKLENDİ] -> {site}")
        
    print("\nURL Sorguları Yapılıyor...")
    test_url_sorgulari = [
        "sahte-banka-giris.net",      # Listede var (Kesinlikle Bulundu)
        "google.com",                  # Listede yok (Kesinlikle Yok demesini bekliyoruz)
        "bedava-hediye-kazan.org",    # Listede var (Kesinlikle Bulundu)
        "github.com"                   # Listede yok (Kesinlikle Yok demesini bekliyoruz)
    ]
    
    for url in test_url_sorgulari:
        sonuc = phishing_filter.query(url)
        if sonuc:
            print(f"URL: '{url}' --> ⚠️ Muhtemelen VAR (Zararlı site olabilir, veritabanına bakılıyor!)")
        else:
            print(f"URL: '{url}' --> ✅ Kesinlikle YOK (Güvenli site, doğrudan sayfaya git!)")

    print("-" * 60)

    # -------------------------------------------------------------------------
    # SENARYO 2: Büyük Metin Arşivlerinde Kelime / Belge Filtreleme
    # -------------------------------------------------------------------------
    print("\n--- SENARYO 2: Büyük Metin Arşivinde Kelime Filtreleme ---")
    
    text_capacity = 10000
    text_error_rate = 0.01
    
    archive_filter = BloomFilter(capacity=text_capacity, error_rate=text_error_rate)
    
    # Arşivde geçen yasaklı veya özel anahtar kelimeler
    ozel_kelimeler = ["kriptografi", "algoritma", "olasiliksal", "hash", "optimizasyon"]
    
    for kelime in ozel_kelimeler:
        archive_filter.add(kelime)
        print(f"[ARŞİVE EKLENDİ] -> {kelime}")
        
    print("\nMetin Arşivi Sorguları Yapılıyor...")
    test_kelime_sorgulari = [
        "algoritma",     # Arşivde var
        "bilgisayar",    # Arşivde yok
        "hash",          # Arşivde var
        "yapayzeka"      # Arşivde yok
    ]
    
    for kelime in test_kelime_sorgulari:
        sonuc = archive_filter.query(kelime)
        if sonuc:
            print(f"Kelime: '{kelime}' --> 📄 Muhtemelen Arşivde Var (Detaylı arama başlatılabilir)")
        else:
            print(f"Kelime: '{kelime}' --> ❌ Kesinlikle Arşivde Yok (Diske/Veritabanına hiç bakma)")

    print("=" * 60)

if __name__ == "__main__":
    main()