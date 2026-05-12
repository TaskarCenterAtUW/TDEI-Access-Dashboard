from tdei_auth import authenticate

try:
    token = authenticate()
    print("Authentication successful.")
except (ValueError, ConnectionError) as e:
    print(f"Authentication failed: {e}")