# Proyek Komputer - Indonesia Online Gambling Money Mule Accounts 2026

Proyek ini dilakukan untuk program Kekayaan Intelektual. Proyek ini bertujuan untuk melakukan analisis data eksploratif (EDA) dan membangun dashboard interaktif menggunakan Streamlit.

## Link Live Dashboard
Aplikasi dashboard interaktif dapat diakses melalui tautan berikut:
- **Streamlit App:** https://proyek-komputer-hrzjtcebbqbffljmadpxgq.streamlit.app/

---

## Deskripsi Proyek
Proyek ini menganalisis dataset **Indonesia Online Gambling Money Mule Accounts 2026** untuk menjawab beberapa pertanyaan bisnis utama:
1. **Pertanyaan 1:** Pada rekening yang terindikasi judi online (money mule), kombinasi primary_transaction_channel dan kyc_verification_status mana yang memiliki rata-rata late_night_transaction_ratio dan passthrough_velocity_pct tertinggi, serta berapa jumlah rekening pada kombinasi tersebut, sehingga tim Fraud & Risk Engine dapat memprioritaskan aturan pemblokiran otomatis (automated freeze rule) pada kombinasi kanal dan status KYC yang paling berisiko?
2. **Pertanyaan 2:** Jenis institusi keuangan (institution_type) mana yang memiliki jumlah dan proporsi rekening terindikasi judi online tertinggi serta rata-rata aml_composite_risk_score tertinggi, sehingga tim kepatuhan dapat memprioritaskan audit dan pemantauan tambahan pada institusi tersebut?
3. **Pertanyaan 3:** Indikator anomali utama (primary_anomaly_indicator) apa yang paling dominan pada rekening terindikasi judi online, dan bagaimana kaitannya dengan klasifikasi risiko akun, sehingga tim deteksi dapat memprioritaskan pembangunan aturan deteksi (detection rule) berdasarkan pola anomali tersebut?
---

## Struktur Direktori
```text
.
├── dashboard/
│   └── dashboard.py
├── data/
│   └── indonesia_online_gambling_mule_accounts_enriched_2026.csv
├── Alif Setyo Wisnuaji_Proyek Komputer_HKI.ipynb
├── README.md
├── requirements.txt
├── streamlit_logs.txt
└── url.txt
```

---

## Cara Menjalankan Dashboard Secara Lokal

### 1. Prasyarat (Prerequisites)
Pastikan Anda telah menginstal **Python 3.8+** di perangkat Anda.

### 2. Clone atau Unduh Repositori
```bash
git clone https://github.com/Rambutanku/proyek-komputer.git
cd proyek-komputer
```

### 3. Buat dan Aktifkan Virtual Environment (Opsional tetapi Disarankan)
* **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Instal Dependency
Instal seluruh library yang dibutuhkan dengan menjalankan perintah berikut:
```bash
pip install -r requirements.txt
```

### 5. Jalankan Aplikasi Streamlit
Masuk ke direktori `dashboard` (jika file `dashboard.py` berada di dalam folder tersebut) atau jalankan langsung perintah:
```bash
streamlit run dashboard/dashboard.py
```
Aplikasi akan secara otomatis terbuka di peramban (browser) default Anda di alamat `http://localhost:8501`.


### Daftar Pustaka
```bibtex
@dataset{muthathohirin2026online_gambling_forensics,
  author       = {Luthfi Muthathohirin},
  title        = {Indonesia Online Gambling Transactions and Money Mule Accounts: 2026 Forensic Benchmark},
  year         = {2026},
  publisher    = {Kaggle},
  url          = {https://www.kaggle.com/datasets/luthfimuthathohirin/indonesia-online-gambling-bank-accounts-forensics},
  license      = {Creative Commons Zero v1.0 Universal}
}
```
