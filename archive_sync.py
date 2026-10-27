import os
import time
import re
from bloom_filter.filter import BloomFilter

# 1. Metin Arşivi için Bloom Filter Motoru (Kapasite: 200.000 Kelime)
archive_filter = BloomFilter(capacity=200000, error_rate=0.0001)

# İzlenecek Kurumsal Arşiv Klasörü
ARCHIVE_FOLDER = "./archive_folder"

def tokenize_text(text):
    """Metindeki kelimeleri ayıklar ve temizler"""
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)

def start_archive_sync_daemon():
    os.makedirs(ARCHIVE_FOLDER, exist_ok=True)
    print(f"📚 OmniFilter Arşiv & RAG Senkronizatör Ajanı Başlatıldı!")
    print(f"📂 İzlenen Arşiv Dizin: {os.path.abspath(ARCHIVE_FOLDER)}")
    print(f"⚡ 7/24 Metin Dizine Ekleme ve Belge İndeksleme Aktif... (Çıkış için CTRL+C)\n")
    
    indexed_files = set()
    
    # Başlangıçta klasördeki mevcut belgeleri tara
    for file_name in os.listdir(ARCHIVE_FOLDER):
        file_path = os.path.join(ARCHIVE_FOLDER, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    words = tokenize_text(f.read())
                    for word in words:
                        archive_filter.add(word)
                indexed_files.add(file_name)
                print(f"📖 Pre-Index: '{file_name}' içerisindeki {len(words)} benzersiz kelime bellege eklendi.")
            except Exception as e:
                pass

    print(f"\n✅ Hazır! Yeni belge akışı bekleniyor...\n")

    while True:
        try:
            current_files = set(os.listdir(ARCHIVE_FOLDER))
            new_files = current_files - indexed_files
            
            for file_name in new_files:
                file_path = os.path.join(ARCHIVE_FOLDER, file_name)
                time.sleep(0.5)
                
                if os.path.isfile(file_path):
                    print(f"\n[📄 YENİ DOKÜMAN TESPİT EDİLDİ]: {file_name}")
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            words = tokenize_text(content)
                            
                            start_time = time.time()
                            for word in words:
                                archive_filter.add(word)
                            elapsed_time = (time.time() - start_time) * 1000
                            
                            print(f"   ↳ İndeksleme Tamamlandı: {len(words)} kelime belleğe işlendi.")
                            print(f"   ↳ İndeksleme İşlem Süresi: {elapsed_time:.4f} ms")
                            print(f"   🧠 RAG Yapay Zeka Ön Belleği Güncellendi.")
                            
                    except Exception as e:
                        print(f"   ❌ Hata: Dosya okunamadı ({e})")
                    
                    indexed_files.add(file_name)
                    
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n🛑 Arşiv Ajanı durduruldu.")
            break

if __name__ == "__main__":
    start_archive_sync_daemon()