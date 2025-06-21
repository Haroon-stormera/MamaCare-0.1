# MamaCare-0.1
# 🧬 MamaCare 0.1 – Liver Cancer Risk Prediction (Streamlit Web App)

*Powered by StageZero AI | Built with ❤ in Pakistan*

MamaCare is an early-stage health-tech project focused on affordable and accessible cancer prediction.  
This is version *0.1, which predicts the **risk level of liver cancer (Low, Medium, High)* based on 12 clinical symptoms using a machine learning model.

> 🚀 Our mission: *Detect before it's too late.* Help families act early. Build a digital hospital for the underserved.

---

## 💡 What is MamaCare 0.1?

MamaCare 0.1 is a simple *Streamlit-based web application* powered by a *Random Forest classifier* trained on a custom dataset of liver cancer symptoms.

Users can enter their details (e.g., fatigue, jaundice, hepatitis history, etc.) and the app will predict their liver cancer risk.

---

## 📊 Dataset

- 📁 File: MamaCare_LiverCancer_Dataset.ods
- 🧪 Total Samples: 16,000+
- 🧬 Features: 12 (e.g., fatigue, nausea, hepatitis, weight loss)
- 🎯 Labels: Low, Medium, High risk (balanced using SMOTE)

---

## 🔧 Technologies Used

- Python (Pandas, Scikit-learn, Joblib)
- Imbalanced-learn (SMOTE)
- Streamlit (for web app UI)
- GitHub (version control)
- Excel/ODS for dataset format

---

## 🧠 How It Works

1. Load dataset and clean
2. Encode categorical features
3. Apply SMOTE to balance all 3 risk classes
4. Train Random Forest Classifier
5. Build Streamlit UI for live prediction
6. Host locally for testing

---

## 🖥 How to Run It Locally

```bash
# Clone the repo
git clone https://github.com/your-username/MamaCare-0.1.git
cd MamaCare-0.1

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # for Windows

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
