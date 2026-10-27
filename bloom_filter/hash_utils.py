import mmh3

def generate_hashes(item: str, k: int, m: int) -> list:
    """
    Verilen bir eleman (item) için k adet bağımsız hash indisi üretir.
    m: Bit dizisinin toplam boyutu
    k: Kullanılacak hash fonksiyonu (seed) sayısı
    """
    indexes = []
    for i in range(k):
        # mmh3.hash işlevine farklı seed (i) vererek bağımsız sonuçlar elde ediyoruz.
        # Çıkan sonucun negatif olabilme ihtimaline karşı abs() alıyoruz 
        # ve m'e göre modunu alarak bit dizisi içinde bir indis buluyoruz.
        hash_val = abs(mmh3.hash(str(item), seed=i))
        index = hash_val % m
        indexes.append(index)
        
    return indexes