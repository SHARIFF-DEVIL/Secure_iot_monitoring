import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Load sensor data
df = pd.read_csv("data/sensor_data.csv")
X = df[["temperature", "humidity", "gas"]]

# Create and train model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X)

# Save the model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/anomaly_model.pkl")

print("[✔] ML model trained and saved to 'model/anomaly_model.pkl'")
