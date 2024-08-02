from sentence_transformers import util

from text_preprocessing import preprocess_text, generate_ngrams


def match_skills(text, predefined_skills, model, threshold=0.90):
    text = preprocess_text(text)
    ngrams = generate_ngrams(text, n=4)
    predefined_skills_list = list(predefined_skills)
    # Encode all n-grams and predefined skills in one batch
    ngram_embeddings = model.encode(list(ngrams), convert_to_tensor=True)
    skill_embeddings = model.encode(predefined_skills_list, convert_to_tensor=True)

    # Compute cosine similarity in one go
    cosine_scores = util.pytorch_cos_sim(ngram_embeddings, skill_embeddings)
    cosine_scores = cosine_scores.cpu().numpy()

    matched_skills = set()  # Use a set to store unique matched skills

    # Compare n-grams with predefined skills and filter by similarity threshold
    for i, scores in enumerate(cosine_scores):
        for j, score in enumerate(scores):
            if score >= threshold:
                matched_skills.add(predefined_skills_list[j])

    return list(matched_skills)
