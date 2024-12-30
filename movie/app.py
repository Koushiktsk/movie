import pickle
import streamlit as st
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


st.header('Movie Recommender System')
movies = pickle.load(open('model/movie_list.pkl','rb'))
movies = pd.DataFrame(movies)
similarity = pickle.load(open('model/similarity.pkl','rb'))

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations[1:6]:
        st.write(i)





