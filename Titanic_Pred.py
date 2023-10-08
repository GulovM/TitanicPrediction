import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Titanic Prediction",
    page_icon="🚢",
    layout="wide", 
    initial_sidebar_state="expanded", 
)

image = Image.open("Titanic.png")
st.image(image)
st.title("Titanic survivors prediction")
st.subheader('This is a program to predict whether you or someone else would survive if you were on the Titanic')

model_selected = st.radio('What analysis do you want to use', ('KNeighborsClassifier', 'LogisticRegression', 'DecisionTreeClassifier', 'RandomForestClassifier(without options)', 'RandomForestClassifier(with options)', 'Default'))

if model_selected == 'DecisionTreeClassifier':
    pickle_in = open("Titanic_ModelTree.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected in ['LogisticRegression', 'Default']:
    pickle_in = open("Titanic_LogReg.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(with options)':
    pickle_in = open("Titanic_Forest(par).pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(without options)':
    pickle_in = open("Titanic_Forest.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'KNeighborsClassifier':
    pickle_in = open("Titanic_KNN.pkl","rb")
    classifier=pickle.load(pickle_in)

def predict_note_authentication(gender, Age, SibSp, Fare):
    prediction=classifier.predict([[gender, Age, SibSp, Fare]])
    print(prediction)
    return prediction
def main():
    st.title("Titanic survivors prediction")
    gender = st.radio('What is your gender?(0 - male, 1 - female)', (0, 1))
    Age = st.number_input('How old are you?', step=1, value=0)
    SibSp = st.number_input('Number of siblings(Enter only the number)', step=1, value=0)
    Fare = st.number_input('How much could you buy a ticket for(Enter only the number)')

    result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(gender, Age, SibSp, Fare))


    #st.success('The output is {}'.format(result))
    st.success('Prediction that you will survive is(1 - survived, 0 - dead) {}'.format(result))
    
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")


if __name__=='__main__':
    main()
