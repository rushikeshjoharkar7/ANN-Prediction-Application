import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly_express as px

def show_graphs_page():
    
    data = pd.read_csv("fibre_properties.csv")
    del data["Sr.No"]
    
    x_axis_val=st.selectbox('Select X_axis Value', options=["2.5% span length (mm)", "UR (%)","Fineness (ug/inch)", "Bundle Strength (cN/tex)","Trash content (%)","Yarn Count (tex)"])
    
    y_axis_val=st.selectbox('Select Y_axis Value', options=["Lea strength (kg)", "CSP","CV% of count", "CV% strength","Unevenness (CV)","Total imperfections per km"])

    col=st.color_picker('Select a plot colour')
    
    plot = px.scatter(data,x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    
    st.plotly_chart(plot)
    
    
    
  
    
    
        
  
    
    
  

    
    
    
    
    
    
    
   