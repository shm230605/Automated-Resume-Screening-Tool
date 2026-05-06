# src/ingestion.py

# Safe imports
try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    from docx import Document
except ImportError:
    Document = None


def extract_text(file_path):
    """
    Extract text from PDF, DOCX, or TXT files
    """

    try:
        # -------- PDF --------
        if file_path.endswith(".pdf"):
            if pdfplumber is None:
                print("⚠️ pdfplumber not installed")
                return ""

            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            return text

        # -------- DOCX --------
        elif file_path.endswith(".docx"):
            if Document is None:
                print("⚠️ python-docx not installed")
                return ""

            doc = Document(file_path)
            return "\n".join(p.text for p in doc.paragraphs)

        # -------- TXT --------
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        else:
            print(f"Unsupported file: {file_path}")
            return ""

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""