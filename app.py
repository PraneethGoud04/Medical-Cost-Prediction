import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
with open(r'Medical Insurance Cost Prediction Project.pkl', "rb") as f:
    final_model = pickle.load(f)

# Page Configuration
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide"
)

# Background Styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

h1 {
    color: #1f2937;
}

</style>
""", unsafe_allow_html=True)


# Title
st.title("🏥 Annual Medical Cost Prediction System")

st.markdown("""
Predict annual medical insurance cost using Machine Learning.
""")

# Healthcare Banner Image
st.image(
    "Gemini_Generated_Image_i716wzi716wzi716.png",
    width=1200
)

# Sideba
st.sidebar.header("🩺 Enter Patient Details")

# User Inputs
monthly_premium = st.sidebar.number_input(
    "Monthly Insurance Premium (₹)",
    min_value=0.0,
    value=8500.0,
    step=10.0
)

annual_premium = st.sidebar.number_input(
    "Annual Insurance Premium (₹)",
    min_value=0.0,
    value=102000.0,
    step=10.0
)

total_claims_paid = st.sidebar.number_input(
    "Total Insurance Claims Paid (₹)",
    min_value=0.0,
    value=250000.0,
    step=100.0
)

avg_claim_amount = st.sidebar.number_input(
    "Average Claim Amount (₹)",
    min_value=0.0,
    value=45000.0,
    step=100.0
)

risk_score = st.sidebar.slider(
    "Overall Health Risk Score",
    min_value=0.0,
    max_value=1.0,
    value=0.82
)

is_high_risk = st.sidebar.selectbox(
    "High Risk Patient?",
    ["No", "Yes"]
)

days_hospitalized_last_3yrs = st.sidebar.number_input(
    "Total Hospitalization Days (Last 3 Years)",
    min_value=0,
    value=12
)

# Convert Yes/No to 0/1
is_high_risk = 1 if is_high_risk == "Yes" else 0

# Chronic diseases
chronic_count = st.sidebar.number_input(
    "Number of Chronic Diseases",
    min_value=0,
    value=1
)

# Create dataframe
input_data = pd.DataFrame({
    'monthly_premium': [monthly_premium],
    'annual_premium': [annual_premium],
    'total_claims_paid': [total_claims_paid],
    'avg_claim_amount': [avg_claim_amount],
    'risk_score': [risk_score],
    'chronic_count': [chronic_count],
    'is_high_risk': [is_high_risk],
    'days_hospitalized_last_3yrs': [days_hospitalized_last_3yrs]
})

# Show Input Data
st.subheader("📋 Entered Details")

display_data = pd.DataFrame({
    "Monthly Premium (₹)": [monthly_premium],
    "Annual Premium (₹)": [annual_premium],
    "Total Claims Paid (₹)": [total_claims_paid],
    "Average Claim Amount (₹)": [avg_claim_amount],
    "Health Risk Score": [risk_score],
    "High Risk Patient": ["Yes" if is_high_risk == 1 else "No"],
    "Hospitalization Days (3 Years)": [days_hospitalized_last_3yrs]
})

st.dataframe(display_data)

# Prediction
if st.button("🔍 Predict Medical Cost"):

    prediction = final_model.predict(input_data)

    st.success(
        f"💰 Predicted Annual Medical Cost: ₹ {prediction[0]:,.2f}"
    )

    st.balloons()
