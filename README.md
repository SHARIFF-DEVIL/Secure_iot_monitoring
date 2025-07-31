# 🔐 Secure IoT Monitoring System

A complete **AI-driven, secure, and scalable IoT Monitoring System** built using **Python, Streamlit, SQLite**, and **data encryption techniques** — designed for smart environments where **real-time sensor data** integrity and monitoring are critical.

## 🚀 Features

- 📡 **Multi-Sensor Simulation**  
  Realistic simulation of multiple IoT sensors (temperature, humidity, gas levels).

- 🔒 **AES Encryption**  
  End-to-end encryption of sensor data before database storage.

- 📊 **Interactive Streamlit Dashboard**  
  Visualizes real-time sensor data in an intuitive and user-friendly format.

- 🎯 **Sensor Filtering**  
  Select and display data from specific sensor IDs using a dropdown and Apply button.

- 📁 **Lightweight SQLite Storage**  
  Stores encrypted sensor logs locally with simple schema.

- 🔐 **Session Logout Button**  
  Simulates logout functionality to clear user sessions.

- 🧩 **Modular Structure**  
  Clean and scalable Python architecture with reusable components.

---

## 📁 Project Structure

secure-iot-monitoring/
├── app/
│ └── dashboard.py # Streamlit dashboard
├── scripts/
│ ├── simulate_receiver.py # Sensor data simulation (with encryption)
│ └── encryption_utils.py # AES key management & encryption logic
├── database/
│ └── sensor_logs.db # SQLite database file
├── secret.key # Generated AES encryption key
└── README.md

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**
- **SQLite**
- **Pandas**
- **Cryptography (AES)**

---
