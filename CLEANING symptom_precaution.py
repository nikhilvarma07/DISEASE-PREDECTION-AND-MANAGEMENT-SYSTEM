# ===============================
# CLEANING symptom_precaution.csv
# ===============================

import pandas as pd

precaution = pd.read_csv("symptom_precaution.csv")

print("BEFORE CLEANING")
print("Shape:", precaution.shape)
print("Missing values:", precaution.isnull().sum().sum())
print("Duplicate rows:", precaution.duplicated().sum())

# Fill missing precaution values
precaution = precaution.fillna("No precaution available")

print("\nAFTER CLEANING")
print("Shape:", precaution.shape)
print("Missing values:", precaution.isnull().sum().sum())
print("Duplicate rows:", precaution.duplicated().sum())

# Save cleaned file
precaution.to_csv("cleaned_precaution.csv", index=False)