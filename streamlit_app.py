import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman & AI
st.set_page_config(page_title="Deep Learning AI Generator", layout="wide")

# Masukkan API Key Anda di sini
# genai.configure(api_key="PASTE_YOUR_GEMINI_API_KEY_HERE")

def generate_deep_learning_content(topik, mapel, fase):
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Buatkan rancangan kegiatan pembelajaran mendalam (Deep Learning) untuk:
    Topik: {topik}
    Mata Pelajaran: {mapel}
    Fase: {fase}
    
    Rancangan harus mencakup 8 dimensi lulusan berikut secara spesifik untuk topik tersebut:
    1. Character, 2. Citizenship, 3. Collaboration, 4. Communication, 
    5. Creativity, 6. Critical Thinking, 7. Compassion, 8. Computational Thinking.
    
    Format dalam bentuk poin-poin yang aplikatif bagi guru.
    """
    
    response = model.generate_content(prompt)
    return response.text

# --- UI APLIKASI ---
st.title("🤖 AI Assistant: Perangkat Pembelajaran Mendalam")
st.markdown("Aplikasi ini menggunakan AI untuk mengintegrasikan **8 Dimensi Lulusan** ke dalam Modul Ajar Anda.")

with st.sidebar:
    st.header("⚙️ Pengaturan")
    api_key = st.text_input("Masukkan Gemini API Key", type="password")
    mapel = st.text_input("Mata Pelajaran", "Biologi")
    fase = st.selectbox("Fase", ["A", "B", "C", "D", "E", "F"])
    topik = st.text_area("Topik/Materi Spesifik", "Dampak Mikroplastik di Laut")
    
    if api_key:
        genai.configure(api_key=api_key)
    
    generate_btn = st.button("Generate Langkah Pembelajaran ✨")

if generate_btn:
    if not api_key:
        st.error("Silakan masukkan API Key terlebih dahulu!")
    else:
        with st.spinner("AI sedang merancang pembelajaran mendalam..."):
            try:
                hasil_ai = generate_deep_learning_content(topik, mapel, fase)
                
                st.markdown("---")
                st.subheader(f"Hasil Rancangan: {topik}")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown("### 📋 Aktivitas Berbasis 8 Dimensi")
                    st.write(hasil_ai)
                
                with col2:
                    st.markdown("### 🛠️ Tool Kit Guru")
                    st.info("**Strategi:** Gunakan model PjBL (Project Based Learning).")
                    st.warning("**Tips:** Fokuskan asesmen pada proses kolaborasi, bukan hanya hasil akhir.")
                    
                    st.download_button(
                        label="Download Modul",
                        data=hasil_ai,
                        file_name=f"Modul_AI_{topik}.txt"
                    )
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
else:
    st.info("Lengkapi data di samping dan klik Generate untuk melihat keajaiban AI.")
