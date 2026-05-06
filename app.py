import streamlit as st
import pandas as pd
import os

from src.ingestion import extract_text
from src.preprocessing import clean_text
from src.scoring import calculate_similarity

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Resume Screening Dashboard",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS (PRO UI)
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    font-size: 32px;
    font-weight: bold;
}
.card {
    padding: 20px;
    border-radius: 10px;
    background-color: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown("<div class='title'>📄 Automated Resume Screening Dashboard</div>", unsafe_allow_html=True)

# -----------------------------
# INPUT SECTION
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Job Description")
    job_desc = st.text_area("Paste Job Description", height=200)

with col2:
    st.subheader("📂 Upload Resumes")
    uploaded_files = st.file_uploader(
        "Upload resumes",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("🚀 Analyze Candidates"):

    if not job_desc:
        st.warning("Please enter job description")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload resumes")
        st.stop()

    names = []
    texts = []

    # Process files
    for file in uploaded_files:
        temp_path = f"temp_{file.name}"

        with open(temp_path, "wb") as f:
            f.write(file.getbuffer())

        text = extract_text(temp_path)
        cleaned = clean_text(text)

        names.append(file.name)
        texts.append(cleaned)

        os.remove(temp_path)

    # Calculate similarity
    scores = calculate_similarity(clean_text(job_desc), texts)

    df = pd.DataFrame({
        "Resume": names,
        "Score": scores
    })

    # Convert to %
    df["Score"] = df["Score"].apply(lambda x: round(x * 100))

    # Status
    df["Status"] = df["Score"].apply(
        lambda x: "Shortlisted" if x >= 60 else "Rejected"
    )

    df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)

    # -----------------------------
    # METRICS
    # -----------------------------
    st.subheader("📊 Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Resumes", len(df))
    col2.metric("Shortlisted", len(df[df["Status"] == "Shortlisted"]))
    col3.metric("Rejected", len(df[df["Status"] == "Rejected"]))

    # -----------------------------
    # TABLE
    # -----------------------------
    st.subheader("📋 Candidate Ranking")

    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # TOP CANDIDATE
    # -----------------------------
    top = df.iloc[0]

    st.success(f"🏆 Top Candidate: {top['Resume']} ({top['Score']}%)")

    # -----------------------------
    # DOWNLOAD
    # -----------------------------
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Results",
        csv,
        "results.csv",
        "text/csv"
    )