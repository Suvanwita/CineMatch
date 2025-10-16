# CineMatch 🎬  
A Content-Based Movie Recommendation System with Streamlit

# Overview

CineMatch is a content-based movie recommendation system built in Python using Streamlit. It analyzes genre, keywords, and overviews to provide smart movie recommendations with plot summaries and posters (powered by OMDB API).

---

## Features

- Content-based recommendations (using genres, keywords, overviews)
- Visual movie wordcloud
- Modern Streamlit UI
- Movie posters and plots via OMDB API
- Modular and maintainable codebase

---

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/Suvanwita/CineMatch.git
    cd CineMatch
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Get an OMDB API Key:**  
   - Request your OMDB API key at [omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
   - Add it to `app.py`:
     ```
     OMDB_API_KEY = "your_real_omdb_key"
     ```

4. *Prepare your movie dataset:*  
   - Place `movies.csv` in the project root.
   - Ensure it has columns: `genres`, `keywords`, `overview`, `title`.

---

# Usage

streamlit run app.py

- Open the provided local URL in your browser.
- Enter a movie name and click "Find Movies".
- Review recommendations with posters and plot summaries.

---

## File Summary

- **app.py**: Streamlit user interface.
- **core.py**: Loads and processes data, builds similarity matrices.
- **recommend.py**: Finds recommended movies.
- **preprocess.py**: Text cleaning.
- **visualize.py**: Visualizes the data corpus.
- **omdb_utils.py**: Fetches movie details/posters from OMDB.

---

## Credits

- OMDB API ([omdbapi.com](http://www.omdbapi.com/))
- Streamlit ([streamlit.io](https://streamlit.io/))
- scikit-learn
- Wordcloud/matplotlib (for visualization)

---

**Enjoy new movie discoveries! 🍿**
