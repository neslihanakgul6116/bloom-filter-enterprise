import time
from bloom_filter.filter import BloomFilter

# 1. WAF (Web Güvenlik Duvarı) için Bloom Filter motorunu başlat
# Bilinen zararlı SQL injection veya XSS imza kalıplarını sisteme yüklüyoruz
waf_filter = BloomFilter(capacity=50000, error_rate=0.0001)

# Bilinen zararlı saldırı imzaları / kalıpları (Örn: Tehlikeli URL parametreleri)
bilinen_saldirilar = [
    "union select 1,2,3",
    "<script>alert('xss')</script>",
    "drop table users",
    "exec(xp_cmdshell)"
]

for saldiri in bilinen_saldirilar:
    waf_filter.add(saldiri)

def simulate_waf_traffic():
    print(f"🌐 OmniFilter Edge WAF Ajanı Başlatıldı!")
    print(f"🛡️ Sistem web trafiğini ve gelen istekleri süzmeye hazır... (Çıkış için CTRL+C)\n")
    
    # Simüle edilecek gelen örnek web istekleri kuyruğu
    gelen_istekler = [
        {"ip": "192.168.1.50", "path": "/index.php?user=admin"},
        {"ip": "10.0.0.15", "path": "/search?q=union select 1,2,3"}, # Zararlı
        {"ip": "172.16.0.8", "path": "/login?user=test&pass=1234"},
        {"ip": "45.33.22.11", "path": "/blog?id=<script>alert('xss')</script>"}, # Zararlı
        {"ip": "192.168.1.100", "path": "/about-us"}
    ]
    
    # Trafik akışını simüle edelim
    for index, istek in enumerate(gelen_istekler, 1):
        time.sleep(1.5) # İstekler arası gerçekçi bekleme süresi
        ip = istek["ip"]
        payload = istek["path"]
        
        print(f"[🌐 İSTEK #{index}] IP: {ip} | Hedef: {payload}")
        
        # Bloom Filter ile milisaniyelik imza taraması
        start_time = time.time()
        is_malicious = waf_filter.query(payload)
        elapsed_time = (time.time() - start_time) * 1000
        
        print(f"   ↳ WAF Filtre Sorgu Süresi: {elapsed_time:.4f} ms")
        
        if is_malicious:
            print(f"   🛑 ENGELLENDİ: Bilinen saldırı imzası tespit edildi! İstek reddedildi (HTTP 403).\n")
        else:
            print(f"   ✅ İZİN VERİLDİ: Trafik temiz. Sunucuya yönlendirildi (HTTP 200).\n")
            
    print("✨ WAF trafik simülasyonu başarıyla tamamlandı.")

if __name__ == "__main__":
    simulate_waf_traffic()