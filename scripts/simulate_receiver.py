import sqlite3
import random
import time
from datetime import datetime

DB_PATH = "database/sensor_logs.db"

def simulate_sensor_data(sensor_id):
    return {
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "gas": round(random.uniform(200, 1000), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def insert_data(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_data (sensor_id, temperature, humidity, gas, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['sensor_id'], data['temperature'], data['humidity'], data['gas'], data['timestamp']))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Simulating sensor data...")
    while True:
        for sensor_id in range(1, 5):  # Simulate 4 sensors
            data = simulate_sensor_data(sensor_id)
            insert_data(data)
            print(f"Sensor {sensor_id} ->", data)
        time.sleep(5)

# --- Logout Button ---
st.sidebar.markdown("---")
if st.sidebar.button("🔓 Logout"):
    st.session_state.clear()  # Clears all session variables
    st.success("You have been logged out.")
    st.experimental_rerun()