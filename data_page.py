import streamlit as st
import pickle
import numpy as np
import pandas as pd

def show_data_page():

    data = pd.read_csv("fibre_properties.csv")
    del data["Sr.No"]

    
    
    st.write(data)



