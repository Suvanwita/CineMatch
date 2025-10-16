import streamlit as st
from core import prepare_data, build_similarity
from recommend import recommend_movies
from visualize import show_wordcloud
from omdb_utils import get_movie_details

OMDB_API_KEY = "your_real_omdb_key" 

st.set_page_config(page_title="CineMatch", layout="centered")
st.title("🎬 CineMatch")
st.subheader("Find your next favorite movie by content similarity.")

df = prepare_data("movies.csv")
show_wordcloud(df['combined'])
cosine_sim = build_similarity(df)

user_input = st.text_input("Enter a movie name", placeholder="e.g. Inception")
search_clicked = st.button("🔎 Find Movies")

if search_clicked:
    if user_input.strip() == "":
        st.warning("Please enter a valid movie name.")
    elif user_input not in df['title'].values:
        st.error("Movie not found in the dataset! Try another title.")
    else:
        st.success(f"Recommendations for {user_input}:")
        recommended_movies = recommend_movies(user_input, cosine_sim, df)
        for movie in recommended_movies:
            plot, poster = get_movie_details(movie, OMDB_API_KEY)
            left, right = st.columns([1, 3])
            with left:
                if poster not in ["N/A", "", None]:
                    st.image(poster)
            with right:
                st.write(f"**{movie}**")
                if plot not in ["N/A", "", None]:
                    st.caption(plot)
            st.write("")
        st.info("Try another title for more movie ideas.")
