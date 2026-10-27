import streamlit as st
from bloom_filter.filter import BloomFilter

# Sayfa Ayarları
st.set_page_config(
    page_title="OmniFilter Enterprise Suite", 
    page_icon="🛡️", 
    layout="wide"
)

# -------------------------------------------------------------------------
# YAN MENÜ (SİDEBAR) - Kurumsal Kimlik ve Hedef Kitleler
# -------------------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/security-checked.png", width=80)
    st.title("OmniFilter Suite")
    st.caption("Çok Katmanlı Kurumsal Bellek & Güvenlik Optimizasyonu")
    
    st.divider()
    
    st.subheader("🎯 Kurumsal Hedef Kitleler")
    
    st.markdown("""
    * **🦠 1. Senaryo (EDR / Malware):**  
      *Siber güvenlik şirketleri, Emniyet Siber Suçlar birimleri ve uç nokta koruma sistemleri.*
    
    * **🌐 2. Senaryo (Edge WAF):**  
      *E-ticaret devleri, büyük web portalları ve CDN sağlayıcıları.*
    
    * **📚 3. Senaryo (Metin Arşivi):**  
      *Arama motorları, RAG tabanlı yapay zeka (LLM) sistemleri, hukuk ve bankacılık arşivleri.*
    """)
    
    st.divider()
    st.info("💡 **Mimari Avantaj:** Devasa veritabanı sorgularını RAM tabanlı ön filtrelemeyle %90 oranında azaltır.")

# Ana Sayfa Başlığı
st.title("🛡️ OmniFilter: Kurumsal Çok Katmanlı Güvenlik ve Optimizasyon Ağ Geçidi")
st.write("Bu arayüz; zararlı yazılım imzalarını, web saldırı kalıplarını ve devasa metin arşivlerini RAM'de milisaniyeler içinde filtreleyen olasılıksal mimariyi simüle eder.")

# Sekmeler
tab1, tab2, tab3, tab4 = st.tabs([
    "🦠 Modül 1: Malware Tespiti (EDR)", 
    "🌐 Modül 2: Edge WAF Filtreleme",
    "📚 Modül 3: Metin Arşivi / RAG Optimizasyonu",
    "⚙️ Performans & İstatistikler"
])

# -------------------------------------------------------------------------
# SEKME 1: Malware (Zararlı Yazılım) Hash Tespiti
# -------------------------------------------------------------------------
with tab1:
    st.header("🦠 Malware Tespiti (EDR / Antivirüs İmzaları)")
    st.write("Milyonlarca zararlı dosya SHA-256 hash'ini istemci RAM'inde tutarak buluta/diske sormadan anında filtreleme yapar.")
    
    if "malware_filter" not in st.session_state:
        st.session_state.malware_filter = BloomFilter(capacity=100000, error_rate=0.0001)
        ornek_hashler = [
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
            "8723633a0121c220f784326b10d458d3d04301a147a1d76ac16ed014fb35db73"
        ]
        for h in ornek_hashler:
            st.session_state.malware_filter.add(h)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("İmza Veritabanına Dosya Hash'i Ekle")
        new_hash = st.text_input("Zararlı SHA-256 Hash", key="input_malware")
        if st.button("Hash Ekle"):
            if new_hash:
                st.session_state.malware_filter.add(new_hash.strip().lower())
                st.success("Zararlı yazılım imza listesine eklendi!")
            else:
                st.warning("Lütfen bir hash değeri girin.")

    with c2:
        st.subheader("Çalıştırılan Dosyayı Tara")
        query_hash = st.text_input("Taranacak Dosya Hash'i", key="query_malware")
        if st.button("Dosyayı Tara"):
            if query_hash:
                sonuc = st.session_state.malware_filter.query(query_hash.strip().lower())
                if sonuc:
                    st.warning("⚠️ **Zararlı Yazılım Olabilir!** (Bulut Sandbox / Derin analize gönderiliyor)")
                else:
                    st.success("✅ **Kesinlikle Temiz.** (Anında çalışmasına izin verildi)")
            else:
                st.warning("Lütfen bir hash değeri girin.")

# -------------------------------------------------------------------------
# SEKME 2: Web & WAF Güvenliği
# -------------------------------------------------------------------------
with tab2:
    st.header("🌐 Web & WAF Güvenliği (Edge Katmanı İstek Filtreleme)")
    st.write("Edge (CDN) sunucularında bilinen zararlı URI, SQL Injection kalıbı ve zararlı IP'leri milisaniyeler içinde engeller.")
    
    if "waf_filter" not in st.session_state:
        st.session_state.waf_filter = BloomFilter(capacity=50000, error_rate=0.001)
        for pattern in ["/admin/config.php", "SELECT * FROM users", "192.168.1.50"]:
            st.session_state.waf_filter.add(pattern)

    c3, c4 = st.columns(2)
    with c3:
        st.subheader("WAF Kara Listesine Kalıp Ekle")
        new_waf = st.text_input("Zararlı URI / SQL Kalıbı / IP", key="input_waf")
        if st.button("WAF'a Ekle"):
            if new_waf:
                st.session_state.waf_filter.add(new_waf)
                st.success("WAF Edge filtresine eklendi!")
            else:
                st.warning("Lütfen bir değer girin.")

    with c4:
        st.subheader("Gelen HTTP İsteğini Denetle")
        query_waf = st.text_input("Gelen İstek Değeri", key="query_waf")
        if st.button("İsteği Denetle"):
            if query_waf:
                sonuc = st.session_state.waf_filter.query(query_waf)
                if sonuc:
                    st.warning("⚠️ **Şüpheli İstek!** (WAF güvenlik motoruna yönlendirildi)")
                else:
                    st.success("✅ **Temiz İstek.** (Sunucuya doğrudan iletildi)")
            else:
                st.warning("Lütfen denetlenecek isteği girin.")

# -------------------------------------------------------------------------
# SEKME 3: Metin Arşivi / RAG Optimizasyonu
# -------------------------------------------------------------------------
with tab3:
    st.header("📚 Büyük Metin Arşivi & RAG Optimizasyon Filtresi")
    st.write("Terabaytlarca döküman arşivinde veya LLM/RAG veritabanında aranan kavramın var olup olmadığını disk okumadan denetler.")
    
    if "text_filter" not in st.session_state:
        st.session_state.text_filter = BloomFilter(capacity=10000, error_rate=0.01)
        for kelime in ["kriptografi", "algoritma", "olasiliksal", "hash", "optimizasyon"]:
            st.session_state.text_filter.add(kelime)

    c5, c6 = st.columns(2)
    with c5:
        st.subheader("Arşive Kelime / Kavram Ekle")
        new_word = st.text_input("Kelime girin", key="input_word")
        if st.button("Kelime Ekle"):
            if new_word:
                st.session_state.text_filter.add(new_word)
                st.success(f"'{new_word}' arşive eklendi!")

    with c6:
        st.subheader("Arşivde Kelime Ara")
        query_word = st.text_input("Aranacak kelime", key="query_word")
        if st.button("Kelime Ara"):
            if query_word:
                sonuc = st.session_state.text_filter.query(query_word)
                if sonuc:
                    st.warning(f"📄 '{query_word}' **Muhtemelen Arşivde Var.** (Detaylı arama başlatıldı)")
                else:
                    st.error(f"❌ '{query_word}' **Kesinlikle Arşivde Yok.** (Veritabanı yorulmadı)")

# -------------------------------------------------------------------------
# SEKME 4: Özel Deneme & İstatistikler
# -------------------------------------------------------------------------
with tab4:
    st.header("⚙️ Sistem Performans & Bellek Optimizasyon Paneli")
    
    cap = st.number_input("Kapasite (n)", value=10000, step=1000, min_value=1, key="custom_cap")
    err = st.number_input("Hata Payı (p)", value=0.001, format="%.4f", min_value=0.0001, max_value=0.9999, key="custom_err")
    
    if err > 0:
        temp_filter = BloomFilter(capacity=cap, error_rate=err)
        
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.info(f"**Hesaplanan Bit Boyutu (m):** {temp_filter.m} bit (~{round(temp_filter.m / 8 / 1024, 2)} KB)")
        with col_stat2:
            st.info(f"**Optimum Hash Sayısı (k):** {temp_filter.k}")
            
        st.success("Milyonlarca veriyi sadece birkaç kilobaytlık bellekte saklayarak %99 RAM ve Disk optimizasyonu elde edilir!")
    else:
        st.error("⚠️ Hata payı (p) 0'dan büyük olmalıdır!")