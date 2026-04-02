# ===============================
# VERIFYING Symptom-severity.csv
# ===============================

import pandas as pd

severity = pd.read_csv("Symptom-severity.csv")

print("Shape:", severity.shape)
print("Missing values:", severity.isnull().sum().sum())
print("Duplicate rows:", severity.duplicated().sum())