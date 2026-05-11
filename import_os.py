import os
import pandas as pd

# Path to your Downloads folder
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Input CSV (change the filename if needed)
input_path = os.path.join(downloads, "Jurisdiction_Codes.csv")

# Output CSV
output_path = os.path.join(downloads, "Jurisdiction_Codes_latest_version.csv")

# Load CSV with no header row
df = pd.read_csv(input_path, header=None, names=["id", "name", "version"])

# Convert version to string
df["version"] = df["version"].astype(str)

# Convert version to sortable tuple
df["version_tuple"] = df["version"].apply(lambda v: tuple(map(int, v.split("."))))

# For each name, keep the row with the highest version
latest = df.loc[df.groupby("name")["version_tuple"].idxmax()]

# Drop helper column
latest = latest.drop(columns=["version_tuple"])

# Save to CSV (id, name, version)
latest.to_csv(output_path, index=False)

print(f"Saved latest versions to: {output_path}")
