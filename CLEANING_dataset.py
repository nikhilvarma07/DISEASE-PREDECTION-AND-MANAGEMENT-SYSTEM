
# ===============================
# CLEANING dataset.csv
# ===============================

import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("BEFORE CLEANING")
print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# 1️⃣ Remove duplicate rows
df = df.drop_duplicates()

# 2️⃣ Fill missing symptom values with 'None'
df = df.fillna("None")

print("\nAFTER CLEANING")
print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# Save cleaned file
df.to_csv("cleaned_dataset.csv", index=False)
