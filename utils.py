import PyPDF2
import pandas as pd
import random as rnd


def read_text_file(file_path):
    """
    Reads a text file and returns its content as a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def get_testing_resume_texts(n=5, random=False):
    # Read the CSV file
    df = pd.read_csv('data/Resume.csv')

    # Convert the 'Resume_html' column to a list
    resume_list = df['Resume_html'].tolist()

    # Check if random sampling is needed
    if random:
        # Return n random elements from the list
        return rnd.sample(resume_list, min(n, len(resume_list)))
    else:
        # Return the first n elements from the list
        return resume_list[:n]


def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Iterate through all the pages and extract text
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text
