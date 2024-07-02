import streamlit as st
import pandas as pd
from surprise import Dataset, Reader, SVD

# Add an image at the top from a URL
image_url = "https://images.app.goo.gl/M3LUbPCwgyB8Ttp2A"
st.image(image_url, caption="Movie Recommender System", use_column_width=True)

# Load your data
links = pd.read_csv('./content/links.csv')
ratings = pd.read_csv('./content/ratings.csv')
movies = pd.read_csv('./content/movies.csv')
tags = pd.read_csv('./content/tags.csv')

# Merge data
data1 = pd.merge(links, ratings, on='movieId', how="outer")
data2 = pd.merge(movies, tags, on='movieId', how="outer")
data = pd.merge(data1, data2, on='movieId', how="outer")

# Ensure proper data types and handle NaNs
data['userId_x'] = data['userId_x'].fillna(-1).astype(int)  # Fill NaNs with a placeholder and convert to int
data['movieId'] = data['movieId'].fillna(-1).astype(int)
data['rating'] = data['rating'].fillna(0).astype(float)
data['timestamp_x'] = pd.to_datetime(data['timestamp_x'], errors='coerce')
data['title'] = data['title'].fillna('Unknown').astype(str)
data['genres'] = data['genres'].fillna('Unknown').astype(str)
data['userId_y'] = data['userId_y'].fillna(-1).astype(int)
data['tag'] = data['tag'].fillna('Unknown').astype(str)
data['timestamp_y'] = pd.to_datetime(data['timestamp_y'], errors='coerce')

# Prepare the data for Surprise
reader = Reader(rating_scale=(0.5, 5.0))
data_surprise = Dataset.load_from_df(data[['userId_x', 'movieId', 'rating']].dropna(), reader)

# Train the SVD model
trainset = data_surprise.build_full_trainset()
model = SVD()
model.fit(trainset)

# Function to get recommendations
def get_recommendations(user_id, model, data, n=5):
    movie_ids = data['movieId'].unique()
    user_rated_movies = data[data['userId_x'] == user_id]['movieId'].tolist()
    movies_to_predict = [movie_id for movie_id in movie_ids if movie_id not in user_rated_movies]

    predictions = [model.predict(user_id, movie_id) for movie_id in movies_to_predict]
    recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:n]
    
    recommended_movie_ids = [rec.iid for rec in recommendations]
    recommended_movies = data[data['movieId'].isin(recommended_movie_ids)][['movieId', 'title']].drop_duplicates()
    
    return recommended_movies

# Streamlit app
st.title("Movie Recommender System")

user_id = st.number_input("Enter your User ID:", min_value=1, step=1)
if st.button("Get Recommendations"):
    recommendations = get_recommendations(user_id, model, data)
    if not recommendations.empty:
        st.write("Top 5 movie recommendations for you:")
        for index, row in recommendations.iterrows():
            st.write(f"{row['title']}")
    else:
        st.write("No recommendations available. Please make sure the User ID is correct.")

# To run the app, execute: streamlit run app.py
