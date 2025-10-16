def recommend_movies(movie_name, cosine_sim, df, top_n=5):
    idx = df[df['title'].str.lower() == movie_name.lower()].index
    if len(idx) == 0:
        return 'Movie not found in dataset!'
    idx = idx[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]
