import streamlit as st
import google.generativeai as genai
from fpdf import FPDF

# --- KONFIGURASI PDF ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'MODUL AJAR KURIKULUM MERDEKA (DEEP LEARNING)', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 11)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 8, label, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 7, body)
        self.ln()

# --- FUNGSI GENERATE AI ---
def generate_deep_learning_content(topik, mapel, fase):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    Buatkan rancangan pembelajaran mendalam untuk Topik: {topik}, Mapel: {mapel}, Fase: {fase}.
    Integrasikan secara spesifik dalam kegiatan inti:
    1. Character, 2. Citizenship, 3. Collaboration, 4. Communication, 
    5. Creativity, 6. Critical Thinking, 7. Compassion, 8. Computational Thinking.
    Gunakan bahasa Indonesia yang formal dan inspiratif.
    """
    response = model.generate_content(prompt)
    return response.text

# --- ANTARMUKA STREAMLIT ---
st.set_page_config(page_title="Deep Learning Pro", layout="centered")

st.title("📄 AI Lesson Planner Pro")
st.markdown("Generate Modul Ajar 8 Dimensi & Ekspor ke PDF")

with st.sidebar:
    st.header("Konfigurasi")
    api_key = st.text_input("Gemini API Key", type="password")
    mapel = st.text_input("Mata Pelajaran", "Fisika")
    fase = st.selectbox("Fase", ["A", "B", "C", "D", "E", "F"])
    topik = st.text_area("Topik Materi", "Energi Terbarukan")
    btn_generate = st.button("Generate & Preview")

if btn_generate:
    if not api_key:
        st.error("Masukkan API Key!")
    else:
        genai.configure(api_key=api_key)
        with st.spinner("Menyusun langkah pembelajaran..."):
            hasil_teks = generate_deep_learning_content(topik, mapel, fase)
            
            # Tampilan di App
            st.subheader("Preview Rancangan")
            st.markdown(hasil_teks)
            
            # Proses PDF
            pdf = PDF()
            pdf.add_page()
            pdf.chapter_title(f"Topik: {topik} ({mapel} - Fase {fase})")
            pdf.chapter_body(hasil_teks)
            
            # Simpan PDF ke variabel
            pdf_output = pdf.output(dest='S').encode('latin-1', 'ignore')
            
            st.download_button(
                label="📥 Unduh PDF Resmi",
                data=pdf_output,
                file_name=f"Modul_Ajar_{topik}.pdf",
                mime="application/pdf"
            )

st.markdown("---")
st.caption("Aplikasi ini membantu guru mengimplementasikan Pembelajaran Mendalam secara sistematis.")
