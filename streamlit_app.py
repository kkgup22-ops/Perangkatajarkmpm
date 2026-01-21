import streamlit as st
import datetime
from datetime import date

# Konfigurasi Halaman
st.set_page_config(page_title="DeepLearn Planner - Kurikulum Merdeka", layout="wide")

# --- JUDUL & HEADER ---
st.title("🎓 DeepLearn Planner: Generator Modul Ajar")
st.markdown("""
**Aplikasi Pembuat Perangkat Pembelajaran Kurikulum Merdeka Berbasis Deep Learning.**
Aplikasi ini membantu guru merancang pembelajaran yang tidak hanya mengejar materi, 
tetapi juga mengasah kompetensi 6C (Character, Citizenship, Collaboration, Communication, Creativity, Critical Thinking).
""")

st.markdown("---")

# --- SIDEBAR: INPUT DATA UMUM ---
with st.sidebar:
    st.header("1. Informasi Umum")
    nama_guru = st.text_input("Nama Penyusun", "Guru Hebat, S.Pd.")
    sekolah = st.text_input("Nama Sekolah", "SMA Merdeka Belajar")
    mata_pelajaran = st.text_input("Mata Pelajaran", "Bahasa Indonesia")
    fase = st.selectbox("Fase / Kelas", ["Fase A (Kls 1-2)", "Fase B (Kls 3-4)", "Fase C (Kls 5-6)", "Fase D (Kls 7-9)", "Fase E (Kls 10)", "Fase F (Kls 11-12)"])
    alokasi_waktu = st.text_input("Alokasi Waktu", "2 x 45 Menit")
    jumlah_siswa = st.number_input("Jumlah Siswa", min_value=1, value=30)

# --- KOLOM UTAMA: INPUT PEDAGOGIS ---
col1, col2 = st.columns(2)

with col1:
    st.header("2. Komponen Inti")
    topik_materi = st.text_input("Topik / Materi Pembelajaran", "Teks Eksposisi")
    tujuan_pembelajaran = st.text_area("Tujuan Pembelajaran (TP)", "Peserta didik mampu menganalisis struktur teks eksposisi...")
    pemahaman_bermakna = st.text_area("Pemahaman Bermakna", "Siswa memahami bahwa argumen yang kuat harus didasari oleh fakta.")

with col2:
    st.header("3. Pendekatan Deep Learning")
    st.info("Pilih kompetensi 6C yang ingin difokuskan dalam modul ini.")
    
    deep_competencies = st.multiselect(
        "Fokus Kompetensi (6C):",
        ["Character (Karakter)", "Citizenship (Kewarganegaraan)", "Collaboration (Kolaborasi)", 
         "Communication (Komunikasi)", "Creativity (Kreativitas)", "Critical Thinking (Berpikir Kritis)"]
    )
    
    model_belajar = st.selectbox("Model Pembelajaran", 
                                 ["Project Based Learning (PjBL)", "Problem Based Learning (PBL)", 
                                  "Inquiry Learning", "Discovery Learning", "Teaching at the Right Level (TaRL)"])

    pertanyaan_pemantik = st.text_input("Pertanyaan Pemantik", "Mengapa kita perlu berargumen dengan sopan?")

# --- LOGIKA GENERATOR ---
def generate_module():
    # Menentukan Strategi Deep Learning berdasarkan input
    strategi_deep = ""
    if "Collaboration (Kolaborasi)" in deep_competencies:
        strategi_deep += "* **Kolaborasi:** Siswa akan bekerja dalam kelompok kecil untuk memecahkan masalah nyata.\n"
    if "Critical Thinking (Berpikir Kritis)" in deep_competencies:
        strategi_deep += "* **Berpikir Kritis:** Siswa diminta menganalisis studi kasus dan memberikan solusi alternatif.\n"
    if "Creativity (Kreativitas)" in deep_competencies:
        strategi_deep += "* **Kreativitas:** Siswa membuat produk/karya orisinil sebagai bentuk pemahaman.\n"
    if not strategi_deep:
        strategi_deep = "* **Umum:** Fokus pada diskusi interaktif dan refleksi."

    # Template Markdown Modul Ajar
    modul_content = f"""
# MODUL AJAR KURIKULUM MERDEKA
## {mata_pelajaran.upper()} - {topik_materi.upper()}

---
### A. INFORMASI UMUM
| Komponen | Keterangan |
| :--- | :--- |
| **Penyusun** | {nama_guru} |
| **Sekolah** | {sekolah} |
| **Fase / Kelas** | {fase} |
| **Alokasi Waktu** | {alokasi_waktu} |
| **Model Pembelajaran** | {model_belajar} |
| **Fokus Deep Learning** | {', '.join(deep_competencies)} |

---
### B. KOMPONEN INTI

#### 1. Tujuan Pembelajaran
{tujuan_pembelajaran}

#### 2. Pemahaman Bermakna
{pemahaman_bermakna}

#### 3. Pertanyaan Pemantik
"{pertanyaan_pemantik}"

---
### C. KEGIATAN PEMBELAJARAN (DEEP LEARNING CYCLE)

#### **Pendahuluan (15 Menit)**
1.  Guru membuka kelas dengan salam dan mengecek kehadiran.
2.  **Apersepsi:** Guru mengajukan pertanyaan pemantik: *"{pertanyaan_pemantik}"*
3.  Guru menyampaikan tujuan pembelajaran dan mengaitkannya dengan kehidupan nyata (**Contextual Learning**).

#### **Kegiatan Inti ({model_belajar})**
*Penerapan Strategi Deep Learning:*
{strategi_deep}

**Langkah-langkah Kegiatan:**
1.  **Orientasi Masalah/Proyek:** Siswa diberikan stimulus terkait {topik_materi}.
2.  **Organisasi Belajar:** Siswa dibagi menjadi kelompok (Fokus pada *Collaboration*).
3.  **Penyelidikan/Eksplorasi:** Siswa mencari informasi menggunakan sumber belajar digital maupun buku teks.
4.  **Mengembangkan Hasil:** Siswa menyusun hasil diskusi (Fokus pada *Creativity* & *Communication*).
5.  **Analisis & Evaluasi:** Kelompok mempresentasikan hasil, kelompok lain menanggapi dengan kritis.

#### **Penutup (15 Menit)**
1.  **Refleksi:** Siswa dan guru menyimpulkan materi.
2.  **Asesmen Formatif:** Kuis singkat atau *Exit Ticket*.
3.  Guru menyampaikan rencana pertemuan berikutnya.

---
### D. ASESMEN
1.  **Asesmen Awal:** Tanya jawab lisan di awal pembelajaran.
2.  **Asesmen Formatif:** Observasi diskusi (Rubrik 6C) dan LKPD.
3.  **Asesmen Sumatif:** Produk/Tes Tulis di akhir lingkup materi.

---
*Dibuat secara otomatis oleh DeepLearn Planner pada tanggal {date.today()}*
    """
    return modul_content

# --- TOMBOL AKSI ---
st.markdown("---")
if st.button("🚀 Buat Modul Ajar Sekarang"):
    if not topik_materi or not tujuan_pembelajaran:
        st.error("Mohon lengkapi Topik Materi dan Tujuan Pembelajaran!")
    else:
        hasil_modul = generate_module()
        
        st.success("Modul Ajar Berhasil Dibuat!")
        st.markdown("### Preview Modul Ajar")
        
        # Tampilkan hasil dalam container dengan border
        with st.container(border=True):
            st.markdown(hasil_modul)
        
        # Tombol Download
        st.download_button(
            label="💾 Download sebagai File Teks",
            data=hasil_modul,
            file_name=f"Modul_Ajar_{topik_materi.replace(' ', '_')}.md",
            mime="text/markdown"
        )
