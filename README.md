# 📱 Understanding MyTelkomsel, the AI Way
Uncovering user sentiment and complaints using IBM Granite-powered analysis

## 📌 Project Overview
Transformasi MyTelkomsel menjadi Super App pada pertengahan 2024—dengan misi menyediakan pengalaman digital yang lebih beragam—justru memicu keluhan besar dari para pengguna.Meski menyumbang >95% transaksi digital Telkomsel, versi terbaru aplikasi ini dinilai lambat, membingungkan, dan tidak stabil.

Proyek ini bertujuan untuk:
a. Memahami sentimen pengguna dari ribuan ulasan di Google Play,
b. Mengidentifikasi keluhan paling krusial dan mendesak,
c. Serta menyusun rekomendasi perbaikan berbasis data, menggunakan kekuatan AI: IBM Granite + dashboard interaktif via Streamlit.

Proyek ini bertujuan untuk menggali sentimen dan keluhan utama pengguna MyTelkomsel menggunakan pendekatan analisis berbasis kecerdasan buatan (AI). Melalui pemrosesan data ribuan ulasan pengguna dan pemodelan menggunakan IBM Granite serta visualisasi di Streamlit, proyek ini membantu mengidentifikasi akar keluhan pengguna, urgensinya, dan memberikan rekomendasi perbaikan yang berbasis data.

## 📂 Raw Dataset Link
Dataset diambil dengan metode scraping dari Google Play Review MyTelkomsel
https://play.google.com/store/apps/details?id=com.telkomsel.telkomselcm&hl=id

## 📊 Insight & Findings

### 💡 Insight & Findings

### 🔴 Sentimen Negatif (93%)
Sebagian besar komentar menunjukkan rasa frustrasi yang tinggi terhadap performa, navigasi, dan kestabilan aplikasi.

Top Issues Identified:
⚠️ Performance/Slow: Aplikasi sering lemot, lag, delay saat buka fitur
🧩 UI/UX Complexity: Tampilan makin ribet, fitur menumpuk, user bingung
💥 Crash & Bugs: Aplikasi force close saat dibuka, data tidak muncul
🔐 Login Issues: OTP gagal, logout sendiri, login ulang berkali-kali
💸 Payment Errors: Pembayaran gagal, saldo tidak terbaca

“Dulu simple. Sekarang ribet dan berat. Fitur makin banyak, tapi gunanya makin sedikit.” – salah satu ulasan populer

### 🟡 Sentimen Netral (6%)
Berisi fakta teknis dan laporan pengalaman yang mendetail, seringkali disertai keluhan ringan atau permintaan perbaikan kecil.

### 🟢 Sentimen Positif (1%)
Sedikit review yang menyampaikan harapan agar aplikasi diperbaiki dan menjadi lebih stabil di masa depan.

### 🧠 Most Agreed Complaints (Top 5)
1. Tidak bisa mengedit informasi personal
2. Aplikasi sangat lambat dan membingungkan
3. Crash terus saat dibuka
4. Harga layanan naik, fitur tidak maksimal
5. Login gagal dan OTP sering error

### 🤖 AI Support Explanation
| Tahap Analisis           | Model AI                   | Fungsi Utama                                               |
| ------------------------ | -------------------------- | ---------------------------------------------------------- |
| Sentiment Classification | IBM Granite 3-8b-instruct  | Menganalisis polaritas sentimen (positif, netral, negatif) |
| Complaint Categorization | IBM Granite (prompt-based) | Mengklasifikasikan ulasan ke 7 kategori keluhan utama      |
| Summarization            | IBM Granite Summarizer     | Merangkum komentar ke dalam narasi insight                 |

### 🧪 Streamlit Dashboard Overview
Dashboard ini dibangun untuk menampilkan hasil analisis sentimen dan keluhan pengguna MyTelkomsel secara interaktif dan visual.

Berikut merupakan dashboard visualisasi insight dari MyTelkomsel
🔗 https://hacktiv8-capstoneproject-mytelkomsel-inkaspuspadarma.streamlit.app/

### ✨ Created with purpose by Inka Sharatu Puspadarma
Hacktiv8 Capstone Project – June 2025
