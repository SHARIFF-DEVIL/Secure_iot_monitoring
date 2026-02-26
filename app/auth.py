import streamlit as st
import hashlib
USER_CREDENTIALS = {
    "admin": "admin123", 
    "iotuser": "iotsecure"
}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
hashed_users = {user: hash_password(pw) for user, pw in USER_CREDENTIALS.items()}
def login(username, password):
    if username in hashed_users and hash_password(password) == hashed_users[username]:
        return True

    return False
