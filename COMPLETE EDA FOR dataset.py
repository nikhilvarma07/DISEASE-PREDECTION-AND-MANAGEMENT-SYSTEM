## EDA For the cleaned_dataset.csv

# ======================================
# PHASE 4 - COMPLETE EDA FOR dataset.csv
# ======================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# 1️⃣ Load cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

print("========== BASIC INFORMATION ==========")
print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("\nColumns:", df.columns.tolist())

# 2️⃣ Number of unique diseases
print("\nNumber of unique diseases:", df["Disease"].nunique())

# ======================================
# 3️⃣ Disease Distribution
# ======================================

plt.figure(figsize=(12,8))
sns.countplot(y="Disease", data=df, order=df["Disease"].value_counts().index)
plt.title("Disease Distribution")
plt.show()

# ======================================
# 4️⃣ Symptom Frequency Analysis
# ======================================

symptom_columns = df.columns[1:]  # all symptom columns

all_symptoms = []
for col in symptom_columns:
    all_symptoms.extend(df[col].tolist())

symptom_counts = Counter(all_symptoms)
symptom_counts.pop("None", None)  # remove placeholder

top_symptoms = pd.DataFrame(symptom_counts.most_common(10),
                            columns=["Symptom", "Count"])

plt.figure(figsize=(8,6))
sns.barplot(x="Count", y="Symptom", data=top_symptoms)
plt.title("Top 10 Most Frequent Symptoms")
plt.show()

# ======================================
# 5️⃣ Convert to Binary Matrix
# ======================================

df_binary = pd.get_dummies(df[symptom_columns].stack()).groupby(level=0).sum()
df_binary["Disease"] = df["Disease"]

print("\nBinary dataset shape:", df_binary.shape)

# ======================================
# 6️⃣ Correlation Heatmap
# ======================================

plt.figure(figsize=(12,8))
sns.heatmap(df_binary.drop("Disease", axis=1).corr(),
            cmap="coolwarm",
            cbar=True)
plt.title("Symptom Correlation Heatmap")
plt.show()

print("\nEDA Completed Successfully.")