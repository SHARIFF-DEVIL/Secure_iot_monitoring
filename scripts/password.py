import streamlit_authenticator as stauth

# List of plaintext passwords to hash
passwords = ["iotadmin123", "iotuser123"]

# Correct usage for newer versions of streamlit-authenticator
hasher = stauth.Hasher()
hashed_passwords = hasher.generate(passwords)

print("Hashed Passwords:")
for i, hashed in enumerate(hashed_passwords):
    print(f"User {i+1}: {hashed}")
