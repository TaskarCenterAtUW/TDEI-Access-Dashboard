import os
import requests

tdei_auth_token = None
if os.getenv("TDEI_AUTH_TOKEN") is not None:
   tdei_auth_token = str(os.getenv("TDEI_AUTH_TOKEN")).replace("'", "")

base_url = "https://api.tdei.us"
if os.getenv("TDEI_BASE_URL") is not None:
   base_url = os.getenv("TDEI_BASE_URL")

tdei_username = ""
if os.getenv("TDEI_USERNAME") is not None:
   tdei_username = str(os.getenv("TDEI_USERNAME")).replace("'", "")

tdei_password = ""
if os.getenv("TDEI_PASSWORD") is not None:
   tdei_password = str(os.getenv("TDEI_PASSWORD")).replace("'", "")

if tdei_auth_token is None:
    credentials = {
        "username": tdei_username,
        "password": tdei_password
    }

    auth_url = str(base_url) + "/api/v1/authenticate"
    headers = {"Content-Type": "application/json"}
    auth_response = requests.post(auth_url, json=credentials, headers=headers)

    if auth_response.status_code == 200:
        tdei_auth_token = auth_response.json().get("access_token")
    else:
        print("Authentication failed:", auth_response.status_code, auth_response.text)
        exit()

if tdei_auth_token:
    print("Authentication successful.")
    headers = {"Authorization": f"Bearer {tdei_auth_token}"}
    print(tdei_auth_token)