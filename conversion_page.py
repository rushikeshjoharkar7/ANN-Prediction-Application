import streamlit as st
import math
import time

def conversion():
        
    #  select measurement
    A = st.selectbox('Measurement unit for conversion',options=("Select","Length","Weight"))

    if A == "Length":
        # input 1       
        num1 = st.number_input(label="Enter length")

        A1 = st.selectbox('Length Unit ',options=("Kilometer","Meter","Centimeter","Milimeter","Yard","Foot","Inch"))

        if A1 == "Kilometer":
            km = num1
            yd = num1 * 1093.61
            m = num1 * 1000
            cm = num1 * 100000
            mm = num1 * 1000000
            ft = num1 * 3280.8399
            inch = num1 * 39370.0787

        if A1 == "Meter":
            m = num1
            yd = num1 * 1.09361
            km = num1 * 0.001
            cm = num1 * 100
            mm = num1 * 1000
            ft = num1 * 3.280
            inch = num1 * 39.370 


        if A1 == "Centimeter":
            cm = num1
            yd = num1 * 0.0109361
            km = num1 * 0.00001
            m = num1 * 0.01
            mm = num1 * 10
            ft = num1 * 0.0328
            inch = num1 * 0.3937


        if A1 == "Milimeter":
            mm = num1
            yd = num1 * 0.00109361
            km = num1 * 0.000001
            m = num1 * 0.001
            cm = num1 *0.1
            ft = num1 * 0.00328
            inch = num1 * 0.03937


        if A1 == "Yard":
            yd = num1
            mm = num1 * 914.3999
            km = num1 * 0.000914399
            m = num1 * 0.9143999
            cm = num1 * 91.43999
            ft = num1 * 2.999999
            inch = num1 * 35.9999999

        if A1 == "Foot":
            ft = num1
            mm = num1 * 304.7999
            km = num1 * 0.000304799
            m = num1 * 0.304799
            cm = num1 * 30.47999
            yd = num1 * 0.33333
            inch = num1 * 11.99999

        if A1 == "Inch":
            inch = num1
            mm = num1 * 25.400000
            km = num1 * 0.000025400000
            m = num1 * 0.025400000
            cm = num1 * 2.5400000
            yd = num1 * 0.027777
            ft = num1 * 0.0833333





        if st.button("Calculate result"):

            st.write("##### in Kilometers = ",km,"km")
            st.write("##### in yards = ",yd,"yd")
            st.write("##### in Meter = ",m,"m")
            st.write("##### in Centimeter = ",cm,"cm")
            st.write("##### in milimeter = ",mm,"mm")
            st.write("##### in foot = ",ft,"ft")
            st.write("##### in inch = ",inch,"inch")

    if A == "Weight":

        # input 1       
        num1 = st.number_input(label="Enter Weight")

        A2 = st.selectbox('Weight Unit',options=("Kilometer","Meter","Centimeter","Milimeter","Yard","Foot","Inch"))

         