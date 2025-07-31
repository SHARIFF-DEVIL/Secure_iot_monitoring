import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config("Secure IoT Monitoring", layout="wide")

# Load data from SQLite DB
@st.cache_data(ttl=10)
def load_data():
    conn = sqlite3.connect("database/sensor_logs.db")
    df = pd.read_sql_query("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 1000", conn)
    conn.close()
    return df[::-1]  # Show oldest first

# Title
st.title("🔒 Secure IoT Monitoring Dashboard")

# Load data
raw_data = load_data()

# --- Sidebar Sensor Filter ---
st.sidebar.markdown("### 🖥️ Select Machine")

# Get sorted unique sensor IDs
sensor_ids = sorted(raw_data['sensor_id'].unique())
sensor_labels = [f"Sensor {sid}" for sid in sensor_ids]
sensor_map = dict(zip(sensor_labels, sensor_ids))

selected_label = st.sidebar.selectbox("Choose a Sensor", sensor_labels)
selected_sensor_id = sensor_map[selected_label]
apply_filter = st.sidebar.button("✅ Apply")

# Session state logic
if "filter_applied" not in st.session_state:
    st.session_state.filter_applied = False
    st.session_state.filtered_data = raw_data

if apply_filter:
    st.session_state.filtered_data = raw_data[raw_data['sensor_id'] == selected_sensor_id]
    st.session_state.filter_applied = True

data = st.session_state.filtered_data

# 📍 Latest Sensor Readings
st.subheader("📍 Latest Sensor Readings")
if not data.empty:
    latest = data.iloc[-1]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📡 Sensor ID", latest['sensor_id'])
    col2.metric("🌡️ Temperature (°C)", f"{latest['temperature']:.2f}")
    col3.metric("💧 Humidity (%)", f"{latest['humidity']:.2f}")
    col4.metric("🔥 Gas Level (PPM)", f"{latest['gas']:.2f}")
else:
    st.warning("No data to show. Try selecting another sensor.")

# 📊 Charts
st.subheader("📈 Sensor Trends")
if not data.empty:
    st.line_chart(data.set_index("timestamp")[["temperature", "humidity", "gas"]])
else:
    st.info("No data available for selected sensor.")

# 📋 Raw Data Table
st.subheader("🧾 Raw Sensor Data")
st.dataframe(data.tail(50), use_container_width=True)
