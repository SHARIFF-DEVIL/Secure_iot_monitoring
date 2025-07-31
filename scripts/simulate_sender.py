import pandas as pd
from encryption_utils import encrypt_message
import os

# Load sensor data
df = pd.read_csv("data/sensor_data.csv")

# Output file to simulate "transmission"
os.makedirs("data", exist_ok=True)
with open("data/encrypted_data.txt", "wb") as out_file:
    for index, row in df.iterrows():
        # Format as CSV row: temp,hum,gas,label,timestamp
        message = f"{row['temperature']},{row['humidity']},{row['gas']},{row['anomaly']},{row['timestamp']}"
        encrypted = encrypt_message(message)
        out_file.write(encrypted + b"\n")

print("[✔] Encrypted sensor data written to 'data/encrypted_data.txt'")