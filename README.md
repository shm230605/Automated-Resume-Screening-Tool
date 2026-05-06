&#x20;**Automated Resume Screening Tool**



An industry-oriented **AI/NLP-powered Resume Screening Dashboard**that automates candidate shortlisting by extracting resume text, matching it against job descriptions, calculating relevance scores, and generating ranked candidate reports.



\---



&#x20;**Project Overview**



Recruiters often receive hundreds of resumes for a single role.



Manual screening is:

⏳ Time-consuming  

❌ Inconsistent  

⚠️ Error-prone  



This project solves that problem by building an \*\*Automated Resume Screening System\*\* using Python and NLP techniques.



&#x20;**💡 Key Features**



\- 📂 Resume Parsing (PDF / DOCX / TXT)

\- 🧹 Text Cleaning \& Preprocessing

\- 🧠 NLP-based Skill Matching

\- 📊 TF-IDF + Cosine Similarity Scoring

\- 📈 Candidate Ranking System

\- ✅ Automatic Shortlisting (Threshold-based)

\- 📋 CSV Report Generation

\- 🎨 Interactive Streamlit Dashboard



\---



&#x20;**Industry Relevance**



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



&#x20;**NLP-Based Matching**



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



&#x20;**Tech Stack**



&#x20;**Programming Language**

\- Python 3.x



&#x20;**Libraries**

\- Pandas

\- NumPy

\- Scikit-learn

\- pdfplumber

\- python-docx

\- Streamlit



&#x20;**NLP / ML Techniques**

\- TF-IDF

\- Cosine Similarity

\- Keyword Matching



\---



&#x20;**Project Structure**



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





\## Workflow



```

Resume Upload

&#x20;  ↓

Text Extraction

&#x20;  ↓

Cleaning

&#x20;  ↓

Skill Extraction

&#x20;  ↓

TF-IDF Vectorization

&#x20;  ↓

Cosine Similarity

&#x20;  ↓

Resume Ranking

&#x20;  ↓

Shortlisting

&#x20;  ↓

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



&#x20;**NLP**

\- Text preprocessing

\- Feature extraction

\- Similarity scoring



\---



&#x20;**Machine Learning**

\- TF-IDF

\- Vectorization

\- Ranking systems



\---



&#x20;**Dashboard Development**

\- Streamlit UI

\- Interactive reporting



\---



&#x20;**Future Enhancements**



Planned upgrades:



\- FastAPI backend

\- PostgreSQL integration

\- BERT embeddings

\- Candidate analytics dashboard

\- Authentication system

\- Multi-job comparison



\---



&#x20;**Author**



Shresthaa Maiti



