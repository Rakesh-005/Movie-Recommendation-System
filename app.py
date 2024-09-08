import streamlit as st
import pickle
import requests

def poster(m_name):
    api_key = '******'
    url = f"http://www.omdbapi.com/?t={m_name}&apikey={api_key}"
    data=requests.get(url)
    data=data.json()
    if data['Response'] == 'True':
        return data['Poster']
    else:
        return "https://via.placeholder.com/300x450?text=No+Poster+Available"

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    recc_movie=[]
    recc_pos=[]
    for i in distance[1:6]:
        movie_name=movies.iloc[i[0]].title
        recc_movie.append(movie_name)
        recc_pos.append(poster(movie_name))
    return recc_movie,recc_pos


movies=pickle.load(open('movies_list.pkl','rb'))
movies_list=movies['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))


st.header('Movie Recommend')
value=st.selectbox('Select movies from dropdown',movies_list)

if st.button('show recommend'):
    movies_names,movies_pos=recommend(value)
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
        st.image(movies_pos[0])
        st.text(movies_names[0])
    with c2:
        st.image(movies_pos[1])
        st.text(movies_names[1])
    with c3:
        st.image(movies_pos[2])
        st.text(movies_names[2])
    with c4:
        st.image(movies_pos[3])
        st.text(movies_names[3])
    with c5:
        st.image(movies_pos[4])
        st.text(movies_names[4])