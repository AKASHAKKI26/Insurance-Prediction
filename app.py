import streamlit as st
from src.prediction import Insurance_Prediction

st.title("Insurance Prediction")
st.write("A machine learning project that analyzes historical data to predict insurance costs.")

Age=st.number_input("Enter the Age",min_value=1,max_value=100)
Annual_Income_LPA=st.number_input("Enter the Annual Income")
Policy_Term_Years=st.number_input("Enter Term Yeras")
Sum_Assured_Lakhs=st.number_input("Enter Sum Assured")

if st.button("Predict"):
    model=Insurance_Prediction()
    result=model.prediction(Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs)
    st.success(result)
    