import pandas as pd
import json

# Load JSON data
with open("info.json", "r") as f:
    info = json.load(f)

sessions = info["sessions"]
departments = info["departments"]
years = info["year"]

# Load CSV data
df = pd.read_csv("students.csv")

# Extract session, department, and year
df["session"] = df["Your Roll Number "].astype(str).str[:2].map(sessions)
df["department"] = df["Your Roll Number "].astype(str).str[2:4].map(departments)
df["year"] = df["Your Roll Number "].astype(str).str[:2].map(years)

# Save updated CSV
df.to_csv("students_updated.csv", index=False)

print("Updated CSV file saved as students_updated.csv")
