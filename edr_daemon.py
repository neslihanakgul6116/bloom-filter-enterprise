import os
import time
import hashlib
from bloom_filter.filter import BloomFilter

# 1. Bloom Filter motorunu başlat ve bilinen zararlı hash'leri yükle
malware_filter = BloomFilter(capacity=100000, error_rate=0.0001)

# Simülasyon için bilinen bazı zararlı imza örnekleri ekleyelim
ornek_zararlilar = [
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
]
for h in ornek_zararlilar:
    malware_filter.add(h)

# İzlenecek hedef klasör (Örn: Masaüstündeki veya proje içindeki bir test klasörü)
TARGET_FOLDER = "./test_downloads"

def calculate_sha256(file_path):
    """Dosyanın SHA-256 hash değerini hesaplar"""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return None

def start_edr_daemon():
    # Klasör yoksa oluştur
    os.makedirs(TARGET_FOLDER, exist_ok=True)
    print(f"🛡️ OmniFilter EDR Ajanı Başlatıldı!")
    print(f"📂 İzlenen Klasör: {os.path.abspath(TARGET_FOLDER)}")
    print(f"⚡ Sistem 7/24 dosya akışını dinliyor... (Çıkış için CTRL+C)\n")
    
    known_files = set(os.listdir(TARGET_FOLDER))
    
    while True:
        try:
            current_files = set(os.listdir(TARGET_FOLDER))
            new_files = current_files - known_files
            
            for file in new_files:
                file_path = os.path.join(TARGET_FOLDER, file)
                # Dosyanın tam olarak inmesini/yazılmasını beklemek için kısa bir gecikme
                time.sleep(0.5)
                
                if os.path.isfile(file_path):
                    print(f"\n[🔍 YENİ DOSYA TESPİT EDİLDİ]: {file}")
                    file_hash = calculate_sha256(file_path)
                    
                    if file_hash:
                        print(f"   ↳ SHA-256: {file_hash}")
                        
                        # Bloom Filter ile anlık sorgu (Hız testi)
                        start_time = time.time()
                        is_suspicious = malware_filter.query(file_hash)
                        elapsed_time = (time.time() - start_time) * 1000 # milisaniye
                        
                        print(f"   ↳ Filtre Sorgu Süresi: {elapsed_time:.4f} ms")
                        
                        if is_suspicious:
                            print(f"   ⚠️ UYARI: '{file}' şüpheli zararlı imza eşleşmesi verdi! Karantinaya alınıyor.")
                        else:
                            print(f"   ✅ Temiz Dosya. Sistem akışına izin verildi.")
            
            known_files = current_files
            time.sleep(1) # Her 1 saniyede bir klasörü kontrol et
            
        except KeyboardInterrupt:
            print("\n🛑 EDR Ajanı durduruldu.")
            break

if __name__ == "__main__":
    start_edr_daemon()