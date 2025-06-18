import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Layout config
st.set_page_config(page_title="📱 Dashboard Review Telkomsel", layout="wide")
st.title("📱 Dashboard Analisis Sentimen & Keluhan MyTelkomsel")
st.markdown("Sumber data: Review pengguna aplikasi MyTelkomsel di Google Play Store")
st.markdown("---")

@st.cache_data
def load_data():
    df_sentiment = pd.read_csv("labeled_review.csv")
    df_kategori = pd.read_csv("complaint_category.csv")
    df_urgency = pd.read_csv("urgency_category.csv")
    df_summary_kategori = pd.read_csv("category_summary.csv")
    df_top5_summary = pd.read_csv("top5_summary.csv")
    return df_sentiment, df_kategori, df_urgency, df_summary_kategori, df_top5_summary

df_sentiment, df_kategori, df_urgency, df_summary_kategori, df_top5_summary = load_data()

# =======================
# 📊 Distribusi Sentimen
# =======================
st.subheader("📊 Distribusi Sentimen Review")
col1, col2 = st.columns([1, 2])

with col1:
    label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
    df_sentiment['label_text'] = df_sentiment['label'].map(label_map)
    sentiment_counts = df_sentiment['label_text'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    ax1.axis('equal')
    st.pyplot(fig1)

with col2:
    st.markdown("📌 **Ringkasan Sentimen**")
    st.dataframe(sentiment_counts.reset_index().rename(columns={'index': 'Sentimen', 'label_text': 'Jumlah'}))

st.markdown("---")

# =======================
# 🔥 Kategori Keluhan
# =======================
st.subheader("🧭 Kategori Keluhan Terbanyak")
kategori_map = {
    1: "Login/Verification",
    2: "Payment/Top-up",
    3: "Crash/Bug/Error",
    4: "Performance/Slow",
    5: "UI/UX/Navigability",
    6: "Package/Data/Promo",
    7: "Other"
}
df_kategori['kategori_text'] = df_kategori['kategori_keluhan'].map(kategori_map)
st.bar_chart(df_kategori['kategori_text'].value_counts())

st.markdown("---")

# =======================
# 🚨 Distribusi Urgensi
# =======================
st.subheader("🚨 Distribusi Tingkat Urgensi")
urgency_counts = df_urgency['urgency_label'].map({1: "Urgent", 0: "Not Urgent"}).value_counts()
st.bar_chart(urgency_counts)

st.markdown("---")

# =======================
# 📚 Ringkasan Keluhan
# =======================
st.subheader("📚 Ringkasan Keluhan Berdasarkan Kategori")
selected_kategori = st.selectbox("Pilih Kategori Keluhan:", df_summary_kategori['kategori'].unique())
summary = df_summary_kategori[df_summary_kategori['kategori'] == selected_kategori]['summary'].values[0]
st.info(summary)

st.markdown("---")

# =======================
# 🏆 Insight Review Terpopuler
# =======================
st.subheader("🏆 Insight dari 5 Review Paling Banyak Disetujui")
st.dataframe(df_top5_summary, use_container_width=True)

st.markdown("---")

# =======================
# ☁️ WordCloud Visual
# =======================
st.subheader("☁️ WordCloud Berdasarkan Kategori Keluhan")

# Format nama file .png sesuai kategori yang dipilih
filename = "wordcloud_mytelkomsel.png"

try:
    image = Image.open(filename)
    st.image(image, caption="WordCloud dari Semua Komplain Review")
except FileNotFoundError:
    st.warning("⚠️ File 'wordcloud_mytelkomsel.png' tidak ditemukan. Pastikan filenya ada di folder yang sama dengan app.py.")
