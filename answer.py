import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your Excel
df = pd.read_excel("knowledge_base.xlsx")

# Questions list
questions = df["Question"].tolist()

# TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions)

def get_answer(user_query):
    user_tfidf = vectorizer.transform([user_query])
    similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    
    best_index = similarities.argmax()
    best_score = similarities[best_index]
    
    # Threshold check (optional)
    if best_score < 0.2:
        return "Sorry, I could not understand your question."

    return df.iloc[best_index]["Answer"]