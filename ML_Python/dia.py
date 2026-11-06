# Dataset: diabetes.csv; target column is Outcome
!mamba install pandas
!mamba install numpy
!mamba install scikit-learn
!mamba install matplotlib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_score, recall_score




df = pd.read_csv("diabetes.csv")
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Treat impossible zero values in selected medical measurements as missing.
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for c in cols:
    if c in X.columns:
        X[c] = X[c].replace(0, X[c].median())
X = X.fillna(X.median())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)
print("Confusion matrix:", confusion_matrix(y_test, pred))
print("Accuracy:", acc)
print("Error rate:", 1 - acc)
print("Precision:", precision_score(y_test, pred, zero_division=0))
print("Recall:", recall_score(y_test, pred, zero_division=0))
