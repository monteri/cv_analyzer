import re
from bs4 import BeautifulSoup


# Function to preprocess the text
def preprocess_text(text):
    # Remove HTML tags if present
    text = BeautifulSoup(text, "html.parser").get_text()

    # Replace hyphenated line breaks (common in PDFs) with a single word
    text = re.sub(r'\b-\s*\n', '', text)

    # Remove line breaks and extra spaces
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)

    # Lowercase the text
    text = text.lower()

    return text


# Function to generate n-grams
def generate_ngrams(text, n=4):
    words = re.findall(r'\b\w+\b', text)
    ngrams = set()
    for i in range(1, n + 1):
        ngrams.update(' '.join(words[j:j + i]) for j in range(len(words) - i + 1))
    return ngrams


# Tests

# Example usage with HTML and PDF artifacts
# job_description_html = """
# <p>We are looking for an <strong>Account Manager</strong> with experience in <i>client management</i>, strategic planning,
# and tools like <a href="#">Microsoft Excel</a> and PowerPoint. Proficiency in English is required.</p>
# """

# Preprocess the text
# cleaned_text = preprocess_text(job_description_html)

# Generate n-grams
# ngrams = generate_ngrams(cleaned_text)

# Output the cleaned text and n-grams for verification
# print("Cleaned Text:", cleaned_text)
# print("Generated N-Grams:", list(ngrams)[:10])