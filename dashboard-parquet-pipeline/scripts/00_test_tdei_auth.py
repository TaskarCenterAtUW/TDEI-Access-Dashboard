import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, REPO_ROOT)

from src.pipeline.tdei_auth import authenticate

try:
    token = authenticate()
    print("Authentication successful.")

except (ValueError, ConnectionError) as e:
    print(f"Authentication failed: {e}")