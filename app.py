import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)

# Load Model
model = joblib.load("loan_model.pkl")

# Sidebar
st.sidebar.title("About")

st.sidebar.info("""
🏦 Loan Approval Prediction

Machine Learning Model:
• Random Forest Classifier

Built using:
• Python
• Scikit-learn
• Streamlit
""")

st.title("🏦 Loan Approval Prediction")

st.write("Enter the applicant details below:")

# Input Columns
col1, col2 = st.columns(2)

with col1:
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
    ApplicantIncome = st.number_input("Applicant Income", min_value=0)

with col2:
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
    LoanAmount = st.number_input("Loan Amount", min_value=0)
    Loan_Amount_Term = st.number_input("Loan Amount Term", value=360)
    Credit_History = st.selectbox("Credit History", [1, 0])
    Property_Area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )

# Encoding
Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0

dep = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}
Dependents = dep[Dependents]

Education = 0 if Education == "Graduate" else 1
Self_Employed = 1 if Self_Employed == "Yes" else 0

area = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}
Property_Area = area[Property_Area]

# Prediction
if st.button("Predict Loan Status"):

    input_data = pd.DataFrame({
        "Gender":[Gender],
        "Married":[Married],
        "Dependents":[Dependents],
        "Education":[Education],
        "Self_Employed":[Self_Employed],
        "ApplicantIncome":[ApplicantIncome],
        "CoapplicantIncome":[CoapplicantIncome],
        "LoanAmount":[LoanAmount],
        "Loan_Amount_Term":[Loan_Amount_Term],
        "Credit_History":[Credit_History],
        "Property_Area":[Property_Area]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")

st.markdown("---")
st.caption("Developed by Ahmed | Machine Learning Portfolio Project")