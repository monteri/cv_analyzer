from sentence_transformers import SentenceTransformer

from match import match_skills
from skills import load_skills
from utils import read_text_file, get_testing_resume_texts, extract_text_from_pdf

if __name__ == "__main__":
    # Load the pre-trained model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    predefined_skills = load_skills()
    # Example job description
    # cv_texts = get_testing_resume_texts()
    cv_texts = [extract_text_from_pdf('cvs/Zadorozhnii_Vladyslav.pdf')]
    job_description = read_text_file('jobs/senior-full-stack.txt')

    # Extract potential skills
    matched_job_skills = match_skills(job_description, predefined_skills, model)


    # Output the matched skills
    print("Job Skills:")
    for skill in matched_job_skills:
        print(f"- {skill}")


    job_skills_number = len(matched_job_skills)
    for cv_text in cv_texts:
        matched_cv_skills = match_skills(cv_text, matched_job_skills, model)
        print("Current CV Skills:")
        for skill in matched_cv_skills:
            print(f"- {skill}")
        print(100 * (len(matched_cv_skills) / job_skills_number))