import os
import pandas as pd

from src.ingestion import extract_text
from src.preprocessing import clean_text
from src.scoring import calculate_similarity


def load_job_description():
    with open("data/job_description.txt", "r", encoding="utf-8") as f:
        return f.read()


def process_resumes(folder):
    names = []
    texts = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if not os.path.isfile(path):
            continue

        text = extract_text(path)
        cleaned = clean_text(text)

        names.append(file)
        texts.append(cleaned)

    return names, texts


def main():
    job_desc = load_job_description()
    job_desc_clean = clean_text(job_desc)

    names, resumes = process_resumes("resumes")

    scores = calculate_similarity(job_desc_clean, resumes)

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

    # -------- PRINT TABLE --------
    print("\n| Resume | Score | Status |")
    print("|--------|-------|--------|")

    for _, row in df.iterrows():
        print(f"| {row['Resume']} | {row['Score']}% | {row['Status']} |")

    # Save
    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/results.csv", index=False)


if __name__ == "__main__":
    main()