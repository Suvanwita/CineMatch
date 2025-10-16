import pandas as pd
from preprocess import preprocess_text
from recommend import recommend_movies
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def prepare_data(csv_path):
    df = pd.read_csv(csv_path)
    required_columns = ['genres', 'keywords', 'overview', 'title']
    df = df[required_columns]
    df = df.dropna().reset_index(drop=True)
    df['combined'] = df['genres'] + ' ' + df['keywords'] + ' ' + df['overview']
    df['cleaned_text'] = df['combined'].apply(preprocess_text)
    return df

def build_similarity(df):
    tfidf_vectorizer = TfidfVectorizer(max_features=500)
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['cleaned_text'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

