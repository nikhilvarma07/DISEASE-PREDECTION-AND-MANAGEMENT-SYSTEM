  ## EDA For the Symptom-severity.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

severity = pd.read_csv("Symptom-severity.csv")

print(severity.head())
print(severity.describe())

print("Shape:", severity.shape)
print("Missing values:", severity.isnull().sum().sum())
print("Duplicate rows:", severity.duplicated().sum())

top_severe = severity.sort_values(by="weight", ascending=False).head(10)

plt.figure(figsize=(8,5))
sns.barplot(x="weight", y="Symptom", data=top_severe)
plt.title("Top 10 Most Severe Symptoms")
plt.show()