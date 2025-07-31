# app/auth.py
import streamlit as st
import hashlib

# Sample user database (you can expand or use SQLite later)
USER_CREDENTIALS = {
    "admin": "admin123",  # plaintext for setup; will hash below
    "iotuser": "iotsecure"
}

# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Generate hashed passwords at runtime (in a real app, pre-hash these!)
hashed_users = {user: hash_password(pw) for user, pw in USER_CREDENTIALS.items()}

# Authentication check
def login(username, password):
    if username in hashed_users and hash_password(password) == hashed_users[username]:
        return True
    return False