import os
import requests
from dotenv import load_dotenv
import json
import geopandas as gpd

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

# Build paths
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
output_path = os.path.join(downloads, "dataset_output.json")

headers = {
    "x-api-key": API_KEY,
    "accept": "application/json"
}

# Query by dataset ID
params = {
    "tdei_dataset_id": "a47f01dd-68e8-40a2-9ba9-409cb83de960"
}

# Make request
response = requests.get(URL, headers=headers, params=params)

data = json.loads(response.text)

table_data = {
    "jurisdiction_id": [],
    "jurisdiction_name": [],
    "state": [],
    "jurisdiction_type": [],
    "population": [],
    "area_sq_km": [],
    "dataset_version": []
}

geometry = [Polygon(data[0]["metadata"]["dataset_detail"]["dataset_area"]["features"][0]["geometry"]["coordinates"])]


# gdf = gpd.GeoDataFrame.from_features(data["features"])
 
# geometry_wkb = [Polygon( response.)






# # Normalize response into a list of items
# if isinstance(data, dict):
#     items = data.get("items", [data])
# elif isinstance(data, list):
#     items = data
# else:
#     raise ValueError("Unexpected API response format")

# # Pretty-print JSON and save to file
# with open(output_path, "w") as f:
#     json.dump(items, f, indent=2)

# print(f"Saved pretty JSON to: {output_path}")





















# import os
# import requests
# from dotenv import load_dotenv
# import json

# load_dotenv()
# API_KEY = os.getenv("API_KEY")
# URL = os.getenv("URL")

# headers = {
#     "x-api-key": API_KEY,
#     "accept": "application/json"
# }

# page_no = 1
# page_size = 50
# all_items = []

# while True:
#     params = {
#       "tdei_dataset_id": "xxxxxxxxxx"
#         # "name": "WSP_",
#         # "full_dataset_name": "WSP_",
#         # "page_no": page_no,
#         # "page_size": page_size
#     }

#     response = requests.get(URL, headers=headers, params=params)
#     data = response.json()

#     # Handle dict or list
#     if isinstance(data, dict):
#         items = data.get("items", [])
#         total_pages = data.get("total_pages")
#     elif isinstance(data, list):
#         items = data
#         total_pages = None
#     else:
#         raise ValueError("Unexpected API response format")

#     print(f"Page {page_no}: {len(items)} items")

#     # Collect items even if some pages are empty
#     all_items.extend(items)

#     # If total_pages exists, use it
#     if total_pages is not None:
#         if page_no >= total_pages:
#             break
#         page_no += 1
#         continue

#     # If no total_pages, stop only when TWO consecutive pages are empty
#     if len(items) == 0:
#         # Try next page to confirm it's really the end
#         params["page_no"] = page_no + 1
#         test = requests.get(URL, headers=headers, params=params).json()

#         # If next page is also empty → real end
#         if (isinstance(test, list) and len(test) == 0) or \
#            (isinstance(test, dict) and len(test.get("items", [])) == 0):
#             break

#     page_no += 1

# print(f"Total items collected: {len(all_items)}")


