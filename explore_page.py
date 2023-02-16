import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def show_explore_page():
    st.title("Properties :- ")

    st.write("""### A.  Lea strength (kg) : """)
    st.write("""##### - The Lea strength of yarn is one of the major properties on which the suitability of yarn for its ultimate end use depends. It is the standard method of measuring the strength of the yarn. The frictional forces rendered to the yarn in the lea test reduce the sensitivity of the test to detect weak places in the yarn. A weak yarn can also produce a low strength, but presence of an abnormally weak place in one of the treads may not be detected.""")
    st.write("""### B.  Count Strength Product (CSP) :  """) 
    st.write("""##### -    This indicator is used to assess the strength of a yarn. Technically, this is the product of count of the yarn and its tensile strength measured using a machine. The higher CSP indicates higher strength of the yarn.""")



