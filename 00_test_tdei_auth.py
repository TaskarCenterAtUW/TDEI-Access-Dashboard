# scripts/00_test_tdei_auth.py

from src.pipeline.tdei_auth import authenticate

if authenticate():
    print("Authenticated successfully.")
else:
    print("Authentication failed.")
