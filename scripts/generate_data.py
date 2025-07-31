import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

os.makedirs("data", exist_ok=True)

num_rows = 1000
anomaly_ratio = 0.1  # 10%

start_time = datetime.now()
timestamps = [start_time + timedelta(seconds=i * 10) for i in range(num_rows)]

def generate_normal():
    return round(np.random.normal(25, 2), 2), round(np.random.normal(50, 5), 2), round(np.random.normal(200, 20), 2)

def generate_anomaly():
    return round(random.uniform(40, 60), 2), round(random.uniform(10, 20), 2), round(random.uniform(400, 600), 2)

data = []
for i in range(num_rows):
    if random.random() < anomaly_ratio:
        temp, hum, gas = generate_anomaly()
        label = 1
    else:
        temp, hum, gas = generate_normal()
        label = 0
    data.append([timestamps[i], temp, hum, gas, label])

df = pd.DataFrame(data, columns=["timestamp", "temperature", "humidity", "gas", "anomaly"])
df.to_csv("data/sensor_data.csv", index=False)

print("[✔] Sensor data generated: data/sensor_data.csv")
