import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regression = data["model"]



def show_predict_page():
    
    
    
    st.title("Yarn Properties Prediction using Linear Regression Model")

    st.write("""### We need some information for Prediction""")

   
    A = st.number_input(label="2.5% span length (mm)",step=1.,format="%.2f")
    B = st.number_input(label="UR (%)",step=1.,format="%.2f")
    C = st.number_input(label="Fineness (ug/inch)",step=1.,format="%.2f")
    D = st.number_input(label="Bundle Strength (cN/tex)",step=1.,format="%.2f")
    E = st.number_input(label="Trash content (%)",step=1.,format="%.2f")
    F = st.number_input(label="Yarn Count (tex)",step=1.,format="%.2f")


    ok = st.button("Predict Yarn Properties")
    
    
    if ok:
        x = np.array([[A,B,C,D,E,F]])
               
        Count = regression.predict(x)
        
        '''st.subheader(f"The estimated Lea strength (kg) is {Count[0,0]:.2f}")
        st.subheader(f"The estimated CSP (Count Strength Product) is {Count[0,1]:.2f}")
        st.subheader(f"The estimated CV% of count is {Count[0,2]:.2f}")
        st.subheader(f"The estimated CV% strength is {Count[0,3]:.2f}")
        st.subheader(f"The estimated Unevenness (CV) is {Count[0,4]:.2f}")
        st.subheader(f"The estimated Total imperfections per km is {Count[0,5]:.2f}")'''
        
        st.write('#### Input Data : ')
        
        st.table(pd.DataFrame({ 
                                'Input Properties': ["2.5% span length (mm)", "UR (%)","Fineness (ug/inch)", "Bundle Strength (cN/tex)","Trash content (%)","Yarn Count (tex)"],
                                'Predicted Values': [A,B,C,D,E,F]
                             }))
        
        st.write('#### Output Data : ')
        
        st.table(pd.DataFrame({ 
                                'Predicted Yarn Properties': ["Lea strength (kg)", "CSP","CV% of count", "CV% strength","Unevenness (CV)","Total imperfections per km"],
                                'Predicted Values': [Count[0,0], Count[0,1], Count[0,2], Count[0,3],Count[0,4],Count[0,5]]
            
                             }))
        
        
        
        #st.caption('### Designed by *Manisha Mogare*')
