import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from graphs_page import show_graphs_page
from data_page import show_data_page
from Calculator import calculator
from ANN_model import show_prediction_page

st.sidebar.title('Explore More')

page = st.sidebar.selectbox("Navigation",("ANN Prediction","Linear Regression Prediction","Properties","Processed Data","Graphical Representation","Calculator"))

if page == "ANN Prediction":
    show_prediction_page()
elif page == "Linear Regression Prediction":
    show_predict_page()
elif page == "Properties" :
    show_explore_page()
elif page == "Processed Data":
    show_data_page()
elif page == "Calculator":
    calculator()      
else:
    show_graphs_page()
