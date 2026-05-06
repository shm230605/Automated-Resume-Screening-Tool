**Automated Resume Screening Tool**



An industry-oriented **AI/NLP-powered Resume Screening Dashboard**that automates candidate shortlisting by extracting resume text, matching it against job descriptions, calculating relevance scores, and generating ranked candidate reports.



\---


**Project Overview**



Recruiters often receive hundreds of resumes for a single role.



Manual screening is:

⏳ Time-consuming  

❌ Inconsistent  

⚠️ Error-prone  



This project solves that problem by building an \*\*Automated Resume Screening System\*\* using Python and NLP techniques.



**💡 Key Features**



\- 📂 Resume Parsing (PDF / DOCX / TXT)

\- 🧹 Text Cleaning \& Preprocessing

\- 🧠 NLP-based Skill Matching

\- 📊 TF-IDF + Cosine Similarity Scoring

\- 📈 Candidate Ranking System

\- ✅ Automatic Shortlisting (Threshold-based)

\- 📋 CSV Report Generation

\- 🎨 Interactive Streamlit Dashboard



\---



**Industry Relevance**



This project simulates the core functionality used by:



\- Applicant Tracking Systems (ATS)

\- HR Tech Platforms

\- Recruitment Automation Tools

\- Talent Intelligence Systems



**Relevant roles:**



\- Python Developer

\- NLP Engineer

\- Data Analyst

\- Automation Engineer

\- HR Tech Developer

\- Machine Learning Engineer



\---



**Features**



**Resume Parsing**

**Supports:**



\- PDF

\- DOCX

\- TXT



\---



**NLP-Based Matching**



Uses:



\- Text preprocessing

\- Skill extraction

\- TF-IDF vectorization

\- Cosine similarity scoring



\---



**Candidate Ranking**



Automatically ranks resumes by relevance.



\---



**Shortlisting Engine**



Candidates are classified as:



\- Shortlisted

\- Rejected



based on configurable thresholds.



\---

**Dashboard Interface**



Interactive Streamlit dashboard with:



\- Resume upload

\- Job description input

\- Candidate analysis

\- Ranking table

\- CSV export



\---



**Tech Stack**


**Programming Language**

\- Python 3.x



**Libraries**

\- Pandas

\- NumPy

\- Scikit-learn

\- pdfplumber

\- python-docx

\- Streamlit



**NLP / ML Techniques**

\- TF-IDF

\- Cosine Similarity

\- Keyword Matching



\---



**Project Structure**



```

Automated-Resume-Screening-Tool/
│
├── config/
│   └── config.py
│
├── data/
│   └── job\_description.txt
│
├── resumes/
│   ├── resume1.txt
│   ├── resume2.txt
│   └── resume3.pdf
│
├── src/
│   ├── \_\_init\_\_.py
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── feature\_engineering.py
│   ├── scoring.py
│   └── utils.py
│
├── outputs/
│   ├── results.csv
│   └── results.json
│
├── logs/
│   └── app.log
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

```

\---

\ Workflow



```

Resume Upload
   ↓
Text Extraction
   ↓
Cleaning
   ↓
Skill Extraction
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity
   ↓
Resume Ranking
   ↓
Shortlisting
   ↓
CSV Report Generation


```





&#x20;**Sample Output**

```

|   **Resume    |Score |   Status**    |

|-------------|------|-------------|

| resume1.txt | 60%  | Shortlisted |

| resume2.txt | 25%  |  Rejected   |

```

\---





**This project demonstrates:**



&#x20;**Python Development**

\- Modular architecture

\- File handling

\- Error handling



\---



**NLP**

\- Text preprocessing

\- Feature extraction

\- Similarity scoring



\---



&#x20;**Machine Learning**

\- TF-IDF

\- Vectorization

\- Ranking systems



\---


**Dashboard Development**

\- Streamlit UI

\- Interactive reporting



\---



**Future Enhancements**



Planned upgrades:



\- FastAPI backend

\- PostgreSQL integration

\- BERT embeddings

\- Candidate analytics dashboard

\- Authentication system

\- Multi-job comparison



\---


**Author**



Shresthaa Maiti



