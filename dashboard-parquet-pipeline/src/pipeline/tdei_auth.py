# src/pipeline/tdei_auth.py

import os
import requests
from dotenv import load_dotenv

def authenticate():
    """
    Authenticates with the TDEI API using username/password or an existing token.
    Returns the auth token if successful, raises an exception otherwise.
    """

    load_dotenv()

    base_url = os.getenv("TDEI_BASE_URL", "https://api.tdei.us")
    auth_token = os.getenv("TDEI_AUTH_TOKEN")
    username = os.getenv("TDEI_USERNAME", "").replace("'", "")
    password = os.getenv("TDEI_PASSWORD", "").replace("'", "")

    if auth_token:
        return auth_token.replace("'", "")

    if not username:
        raise ValueError("TDEI_USERNAME not found in environment variables.")
    if not password:
        raise ValueError("TDEI_PASSWORD not found in environment variables.")

    auth_url = f"{base_url}/api/v1/authenticate"
    headers = {"Content-Type": "application/json"}
    credentials = {"username": username, "password": password}

    try:
        response = requests.post(auth_url, json=credentials, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Auth request failed: {e}")

    if response.status_code == 200:
        token = response.json().get("access_token")
        if not token:
            raise ValueError("Auth succeeded but no access_token in response.")
        return token

    raise ConnectionError(f"Authentication failed: {response.status_code} {response.text}")