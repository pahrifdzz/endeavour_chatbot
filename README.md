# 🚀 Endeavour AI - Discord Bot

Endeavour AI adalah bot Discord cerdas yang ditenagai oleh model **Gemini 2.5 Flash** terbaru. Bot ini dirancang untuk menjadi asisten produktivitas yang mampu menangani diskusi teknis, bantuan pemrograman, hingga percakapan santai secara real-time.



## 🌟 Fitur Utama
* **Gemini 2.5 Flash Engine**: Menggunakan model terbaru (rilis Juni 2025) yang mendukung pemrosesan cepat dan cerdas.
* **Smart Mention & DM**: Bot hanya merespons saat di-mention atau melalui Direct Message (DM) agar menjaga kenyamanan server.
* **Automatic Message Chunking**: Mampu mengirimkan jawaban panjang (lebih dari 2000 karakter) dengan membaginya menjadi beberapa pesan secara otomatis.
* **Programming Expert**: Dibangun oleh pengembang yang berpengalaman dalam web development (PHP & Python).

## 🛠️ Teknologi yang Digunakan
* **Bahasa**: Python 3.13+
* **Library**: `discord.py` (untuk koneksi Discord)
* **API**: Google Gemini API (v1 REST API via `requests`)
* **Environment**: Diuji pada lingkungan lokal menggunakan Python di Windows.

## ⚙️ Cara Instalasi

1. **Clone Repository**
   ```bash
   git clone [https://github.com/username-anda/endeavour-ai.git](https://github.com/username-anda/endeavour-ai.git)
   cd endeavour-ai
   
2. **Install Dependencies**
   ```bash
   pip install discord.py python-dotenv requests
   
3. **Konfigurasi Environment**
   <br>Buat file .env di folder root dan masukkan API Key Anda:
   ```bash
   DISCORD_TOKEN=your_discord_bot_token
   GEMINI_API_KEY=your_gemini_api_key

4. **Jalankan Bot**
   ```bash
   python main.py

## 📸 Dokumentasi
<br>**Mention Response**
<img width="990" height="298" alt="image" src="https://github.com/user-attachments/assets/6c61cc1f-be08-4b2f-a9db-e3da78a5997f" />

**DM Response**
<img width="937" height="272" alt="image" src="https://github.com/user-attachments/assets/d397966f-47f9-4402-bdb0-a68fa0630c9b" />

