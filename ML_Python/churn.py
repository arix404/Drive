# Dataset: Churn_Modelling.csv
!mamba install pandas
!mamba install numpy
!mamba install scikit-learn
!mamba install matplotlib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report


df = pd.read_csv("Churn_Modelling.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Drop unnecessary columns
drop_cols = ["RowNumber", "CustomerId", "Surname"]
df = df.drop(columns=[c for c in drop_cols if c in df.columns])

# Separate input and output
y = df["Exited"]
X = df.drop(columns=["Exited"])

# Handle missing values
X = X.fillna(X.mode().iloc[0])

# Convert categorical data into numerical data
X = pd.get_dummies(X, drop_first=True, dtype=int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create MLP model
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    max_iter=500,
    random_state=42,
    early_stopping=True
)

# Train model
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
print("Classification Report:\n",
      classification_report(y_test, pred, zero_division=0))

print("Improvement: Tune hidden layers, learning rate and max_iter.")
