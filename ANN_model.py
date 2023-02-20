import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
 
    
import numpy as np
import pandas as pd

data = pd.read_csv("fibre_properties.csv")
del data["Sr.No"]    
    
# Separate Target Variable and Predictor Variables
TargetVariable=["Lea strength (kg)","CSP","CV% of count","CV% strength","Unevenness (CV)","Total imperfections per km"]
Predictors=['2.5% span length (mm)', 'UR (%)', 'Fineness (ug/inch)', 'Bundle Strength (cN/tex)', 'Trash content (%)', 'Yarn Count (tex)']
 
X=data[Predictors].values
y=data[TargetVariable].values
 
### Sandardization of data ###
from sklearn.preprocessing import StandardScaler
PredictorScaler=StandardScaler()
TargetVarScaler=StandardScaler()
 
# Storing the fit object for later reference
PredictorScalerFit=PredictorScaler.fit(X)
TargetVarScalerFit=TargetVarScaler.fit(y)
 
# Generating the standardized values of X and y
X=PredictorScalerFit.transform(X)
y=TargetVarScalerFit.transform(y)
 
# Split the data into training and testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# importing the libraries
from keras.models import Sequential
from keras.layers import Dense
 
# create ANN model
model = Sequential()
 
# Defining the Input layer and FIRST hidden layer, both are same!
model.add(Dense(units=5, input_dim=6, kernel_initializer='normal', activation='relu'))
 
# Defining the Second layer of the model
# after the first layer we don't have to specify input_dim as keras configure it automatically
model.add(Dense(units=5, kernel_initializer='normal', activation='tanh'))
 
# The output neuron is a single fully connected node 
# Since we will be predicting a single number
model.add(Dense(6, kernel_initializer='normal'))
 
# Compiling the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Defining a function to find the best parameters for ANN
def FunctionFindBestParams(X_train, y_train, X_test, y_test):
    
    # Defining the list of hyper parameters to try
    batch_size_list=[5, 10, 15, 20]
    epoch_list  =   [5, 10, 50, 100]
    
    import pandas as pd
    SearchResultsData=pd.DataFrame(columns=['TrialNumber', 'Parameters', 'Accuracy'])
    
    # initializing the trials
    TrialNumber=0
    for batch_size_trial in batch_size_list:
        for epochs_trial in epoch_list:
            TrialNumber+=1
            # create ANN model
            model = Sequential()
            # Defining the first layer of the model
            model.add(Dense(units=5, input_dim=6, kernel_initializer='normal', activation='relu'))

            # Defining the Second layer of the model
            model.add(Dense(units=5, kernel_initializer='normal', activation='relu'))

            # The output neuron is a single fully connected node 
            # Since we will be predicting a single number
            model.add(Dense(6, kernel_initializer='normal'))

            # Compiling the model
            model.compile(loss='mean_squared_error', optimizer='adam')

            # Fitting the ANN to the Training set
            model.fit(X_train, y_train ,batch_size = batch_size_trial, epochs = epochs_trial, verbose=0)

            MAPE = np.mean(100 * (np.abs(y_test-model.predict(X_test))/y_test))
            
# Fitting the ANN to the Training set
model.fit(X, y ,batch_size = 15, epochs = 5, verbose=0)

# Generating Predictions on testing data
Predictions=model.predict(X)

# Scaling the predicted Price data back to original price scale
Predictions=TargetVarScalerFit.inverse_transform(Predictions)

# Scaling the y_test Price data back to original price scale
y_orig=TargetVarScalerFit.inverse_transform(y)

# Scaling the test data back to original scale
Test_Data=PredictorScalerFit.inverse_transform(X)



def show_prediction_page():
    
    
    
    st.title("Yarn Properties Prediction using Artificial Neural Network Model")

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
        
        Count = model.predict(x)
        Count = TargetVarScalerFit.inverse_transform(Count)

        
            
        
        '''st.subheader(f"The estimated Lea strength (kg) is {Count[0,0]:.2f}")
        st.subheader(f"The estimated CSP (Count Strength Product) is {Count[0,1]}")
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







