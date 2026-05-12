# src/pipeline/tdei_auth.py

import os
import requests
from dotenv import load_dotenv

def authenticate():
    """
    Authenticates with the TDEI API using an API key.
    Returns True if authentication succeeds, False otherwise.
    Does NOT print or return the token.
    """

    load_dotenv()
    api_key = os.getenv("API_KEY")
    auth_url = os.getenv("AUTH_URL")

    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")
    if not auth_url:
        raise ValueError("AUTH_URL not found in environment variables.")

    headers = {
        "x-api-key": api_key,
        "accept": "application/json"
    }

    response = requests.get(auth_url, headers=headers)

    # Success = 200 OK
    if response.status_code == 200:
        return True

    return False
