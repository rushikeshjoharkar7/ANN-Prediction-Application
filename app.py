import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from graphs_page import show_graphs_page

st.sidebar.title('Explore More')

page = st.sidebar.radio("Navigation",("Predict", "Yarn Properties","Graphical Representation"))


if page == "Predict":
    show_predict_page()
elif page == "Yarn Properties" :
    show_explore_page()
else :
    show_graphs_page()
