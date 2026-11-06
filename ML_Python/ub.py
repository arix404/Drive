# Dataset: uber.csv (or change FILE to your downloaded CSV name)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

FILE = "uber.csv"
df = pd.read_csv(FILE)
df = df.dropna()
df = df[(df["fare_amount"] > 0) & (df["fare_amount"] < 200)]
df = df[(df["passenger_count"] > 0) & (df["passenger_count"] <= 6)]

# Haversine distance from pickup and drop coordinates
def distance(row):
    lat1, lon1, lat2, lon2 = map(np.radians, [
        row["pickup_latitude"], row["pickup_longitude"],
        row["dropoff_latitude"], row["dropoff_longitude"]])
    dlat, dlon = lat2-lat1, lon2-lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 6371 * 2 * np.arcsin(np.sqrt(a))

df = df[(df["pickup_latitude"].between(-90,90)) &
        (df["dropoff_latitude"].between(-90,90)) &
        (df["pickup_longitude"].between(-180,180)) &
        (df["dropoff_longitude"].between(-180,180))]
df["distance_km"] = df.apply(distance, axis=1)
df = df[df["distance_km"] < 100]

print("Rows after preprocessing:", len(df))
print("Outlier check using boxplot")
plt.boxplot(df["fare_amount"])
plt.title("Fare outliers")
plt.show()
print("Correlation:\n", df[["fare_amount","distance_km","passenger_count"]].corr())

X = df[["distance_km", "passenger_count"]]
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    print(name, "R2 =", round(r2_score(y_test, pred), 3), "RMSE =", round(rmse, 3))
