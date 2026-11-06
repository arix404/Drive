# Dataset: sales_data_sample.csv
!mamba install pandas
!mamba install numpy
!mamba install scikit-learn
!mamba install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_score, recall_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA



df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# Use numeric sales-related columns; robustly select common columns if available.
cols = [c for c in ["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"] if c in df.columns]
X = df[cols].dropna()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    inertia.append(model.inertia_)

plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X_scaled)
df.loc[X.index, "Cluster"] = labels
print("Selected K = 3 (change this based on elbow plot)")
print(df[["Cluster"]].value_counts())
