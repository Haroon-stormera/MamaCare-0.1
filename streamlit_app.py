import streamlit as st
import pandas as pd
import joblib
import os

# Load model
model = joblib.load("mamacare_liver_model.pkl")

# Define features
features = ['age', 'gender', 'fatigue', 'abdominal_pain', 'weight_loss', 'loss_of_appetite',
            'nausea', 'jaundice', 'dark_urine', 'alcohol_use', 'hepatitis', 'family_history']

# Load encoders
encoders = {}
for col in features:
    path = f"{col}_encoder.pkl"
    if os.path.exists(path):
        encoders[col] = joblib.load(path)

# Load target encoder
target_encoder = joblib.load("risk_encoder.pkl")

# UI
st.set_page_config(page_title="MamaCare - Liver Cancer Risk", layout="centered")
st.title("🧬 MamaCare - Liver Cancer Risk Predictor")
st.markdown("Powered by StageZero AI")

# Form
with st.form("risk_form"):
    st.subheader("Enter your details:")

    age = st.slider("Age", 0, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    fatigue = st.selectbox("Fatigue", ["Yes", "No"])
    abdominal_pain = st.selectbox("Abdominal Pain", ["Yes", "No"])
    weight_loss = st.selectbox("Weight Loss", ["Yes", "No"])
    loss_of_appetite = st.selectbox("Loss of Appetite", ["Yes", "No"])
    nausea = st.selectbox("Nausea", ["Yes", "No"])
    jaundice = st.selectbox("Jaundice", ["Yes", "No"])
    dark_urine = st.selectbox("Dark Urine", ["Yes", "No"])
    alcohol_use = st.selectbox("Alcohol Use", ["Yes", "No"])
    hepatitis = st.selectbox("Hepatitis", ["Yes", "No"])
    family_history = st.selectbox("Family History", ["Yes", "No"])

    submit = st.form_submit_button("Predict Risk")

if submit:
    # Prepare input
    input_data = {
        "age": age,
        "gender": gender,
        "fatigue": fatigue,
        "abdominal_pain": abdominal_pain,
        "weight_loss": weight_loss,
        "loss_of_appetite": loss_of_appetite,
        "nausea": nausea,
        "jaundice": jaundice,
        "dark_urine": dark_urine,
        "alcohol_use": alcohol_use,
        "hepatitis": hepatitis,
        "family_history": family_history,
    }

    df = pd.DataFrame([input_data])

    # Encode using saved encoders
    for col in df.columns:
        if col in encoders:
            df[col] = encoders[col].transform(df[col])

    # Predict
    pred_encoded = model.predict(df)[0]
    risk = target_encoder.inverse_transform([pred_encoded])[0]

    st.success(f"🩺 Predicted Risk Level: {risk}")