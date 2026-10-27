import math
from bloom_filter.hash_utils import generate_hashes

class BloomFilter:
    def __init__(self, capacity: int, error_rate: float):
        """
        capacity (n): Beklenen maksimum eleman sayısı
        error_rate (p): Kabul edilebilir hata payı (Örn: 0.01 -> %1)
        """
        self.capacity = capacity
        self.error_rate = error_rate
        
        # 1. Adım: Formüle göre m (bit dizisi boyutu) ve k (hash sayısı) hesaplama
        # m = - (n * ln(p)) / (ln(2))^2
        self.m = int(- (capacity * math.log(error_rate)) / (math.log(2) ** 2))
        
        # k = (m / n) * ln(2)
        self.k = int((self.m / capacity) * math.log(2))
        
        # k en az 1 olmalıdır
        if self.k < 1:
            self.k = 1
            
        # Bellekte yer açma: m tane bit için gereken byte sayısı (her byte 8 bittir)
        self.bit_array = bytearray((self.m + 7) // 8)

    def add(self, item: str):
        """3. Adım: Ekleme Operasyonu - Gelen anahtarın k adet hash indisini 1 yapar."""
        indexes = generate_hashes(item, self.k, self.m)
        for index in indexes:
            byte_index = index // 8
            bit_index = index % 8
            # İlgili biti 1 yapmak için bitwise OR (|) ve sola kaydırma kullanıyoruz
            self.bit_array[byte_index] |= (1 << bit_index)

    def query(self, item: str) -> bool:
        """
        4. Adım: Sorgulama Operasyonu
        - Eğer bitlerden en az biri 0 ise: Eleman KESİNLİKLE YOKTUR (False döner).
        - Tüm bitler 1 ise: Eleman MUHTEMELEN VARDIR (True döner).
        """
        indexes = generate_hashes(item, self.k, self.m)
        for index in indexes:
            byte_index = index // 8
            bit_index = index % 8
            # İlgili bit 0 mı diye kontrol ediyoruz
            if not (self.bit_array[byte_index] & (1 << bit_index)):
                return False  # Kesinlikle yok!
                
        return True  # Muhtemelen var!