import pickle
import pandas as pd
import streamlit as st
import requests
from PIL import Image
import base64


Final_DataSet = pickle.load(open('movie_list.pkl' ,'rb'))
Similarity = pickle.load(open('similarity.pkl' , 'rb'))

def FetchMovie_Poster(id):
    URL = f"https://api.themoviedb.org/3/movie/{id}?api_key=75eb0685f1f9140663e33eb0ea57150a&language=en-US"
    Data = requests.get(URL)
    Data = Data.json()
    PosterPath = Data['poster_path']
    Full_Path = "http://image.tmdb.org/t/p/w500/" + PosterPath
    return Full_Path

def Final_Recommendation(Movie_Name):
    Recommended_movies = []
    Recommended_movies_poster = []
    Movie_Match = Final_DataSet[Final_DataSet['title'].str.contains(Movie_Name , case=False)]
    if Movie_Match.empty:
        #print("Movie Not Found!!")
        return "Movie Not Found!!!!"
    Match_Movie_Title = Movie_Match.iloc[0].title
    Movie_Index = Final_DataSet[Final_DataSet['title'] == Match_Movie_Title].index[0]
    Distance = Similarity[Movie_Index]
    Index_List = list(enumerate(Distance))
    Similar_Movies = sorted(Index_List , reverse=True , key= lambda x : x[1])[1:11]
    for x in Similar_Movies:
        Movie_id = Final_DataSet.iloc[x[0]].movie_id
        Recommended_movies_poster.append(FetchMovie_Poster(Movie_id))
        Recommended_movies.append(Final_DataSet.iloc[x[0]].title)
    return Recommended_movies , Recommended_movies_poster



#Back Ground Image and transparent header

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read())
        st.markdown(
            f"""
              <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover;
            }}
            .css-18e3th9 {{
                background-color: rgba(0, 0, 0, 0);  /* Transparent header */
            }}
           
            </style>
            """,
            unsafe_allow_html=True
        )

set_background('BackGround.jpg')

Page_by_img  = """
<style>
[data-testid = "stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(Page_by_img,unsafe_allow_html=True)

Header_Image = Image.open('techma.png')

st.image(Header_Image,width=90)

#st.title('Movie Recommendation System!!')


# Custom title color
st.markdown(
    """
    <style>
    .custom-title {
        color: #FFAA33;  
        font-size: 42px;
        font-weight: bold;
        font-family : 'Courier New', monospace;
    }
    div[data-testid="stTextInput"] label {
        color: #FFAA33; 
        
        font-weight: bold; 
        font-family : 'Courier New', monospace;
    }
       .custom-caption {
        color: #FFAA33; 
        font-size: 14px; 
        font-weight: bold; 
        font-family : 'Courier New', monospace;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="custom-title">Movie Recommendation System</p>', unsafe_allow_html=True)
 


Selected_Movie = st.text_input("Input The Name Of Movie")



if st.button('Display Recommended Movies'):
    Recommended_movies, Recommended_movies_poster = Final_Recommendation(Selected_Movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(Recommended_movies_poster[0])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[0]}</p>', unsafe_allow_html=True)
    with col2:
        st.image(Recommended_movies_poster[1])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[1]}</p>', unsafe_allow_html=True)
    with col3:
        st.image(Recommended_movies_poster[2])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[2]}</p>', unsafe_allow_html=True)
    with col4:
        st.image(Recommended_movies_poster[3])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[3]}</p>', unsafe_allow_html=True)
    with col5:
        st.image(Recommended_movies_poster[4])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[4]}</p>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(Recommended_movies_poster[5])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[5]}</p>', unsafe_allow_html=True)
    with col2:
        st.image(Recommended_movies_poster[6])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[6]}</p>', unsafe_allow_html=True)
    with col3:
        st.image(Recommended_movies_poster[7])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[7]}</p>', unsafe_allow_html=True)
    with col4:
        st.image(Recommended_movies_poster[8])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[8]}</p>', unsafe_allow_html=True)
    with col5:
        st.image(Recommended_movies_poster[9])
        st.markdown(f'<p class="custom-caption">{Recommended_movies[9]}</p>', unsafe_allow_html=True)