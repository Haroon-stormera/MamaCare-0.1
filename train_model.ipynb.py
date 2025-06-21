import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
import joblib
import os

# 1. Load dataset
data = pd.read_excel("MamaCare_LiverCancer_Dataset.ods", engine="odf")

# 2. Drop missing
data = data.dropna()

# 3. Encode and save encoders
categorical_cols = data.select_dtypes(include='object').columns.drop('risk')
encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le
    joblib.dump(le, f"{col}_encoder.pkl")

# Encode target
target_encoder = LabelEncoder()
data["risk"] = target_encoder.fit_transform(data["risk"])
joblib.dump(target_encoder, "risk_encoder.pkl")

# 4. Features and target
X = data.drop("risk", axis=1)
y = data["risk"]

# 5. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Balance with SMOTE
sm = SMOTE(random_state=42)
X_train_bal, y_train_bal = sm.fit_resample(X_train, y_train)

# 7. Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_bal, y_train_bal)

# 8. Evaluate
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# 9. Save model
joblib.dump(model, "mamacare_liver_model.pkl")
print("✅ Model saved as mamacare_liver_model.pkl")