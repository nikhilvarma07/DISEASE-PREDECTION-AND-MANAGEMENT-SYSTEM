# ===============================
# VERIFYING symptom_Description.csv
# ===============================

import pandas as pd

description = pd.read_csv("symptom_Description.csv")

print("Shape:", description.shape)
print("Missing values:", description.isnull().sum().sum())
print("Duplicate rows:", description.duplicated().sum())