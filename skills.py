import os
import pandas as pd
import pickle


def load_skills():
    skills_file = 'skills/skills_list.pkl'  # File to save/load the skills list
    excel_file_path = 'skills/tech_skills.xlsx'  # Replace with your actual Excel file path

    # Check if the skills file already exists
    if os.path.exists(skills_file):
        # Load the skills list from the file
        with open(skills_file, 'rb') as f:
            skills = pickle.load(f)
        print("Skills list loaded from file.")
    else:
        # Read the skills from the Excel file
        excel_data = pd.read_excel(excel_file_path)

        # Extract the skills from the 'Example' column, lowercase each skill, and remove duplicates
        skills = excel_data['Example'].dropna().str.lower().tolist()

        # Remove duplicates by converting the list to a set and then back to a list
        skills = list(set(skills))

        # Save the skills list to a file for future use
        with open(skills_file, 'wb') as f:
            pickle.dump(skills, f)
        print("Skills list loaded from Excel and saved to file.")

    return skills
