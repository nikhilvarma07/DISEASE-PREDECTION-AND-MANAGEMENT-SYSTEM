## EDA For the symptom_precaution.csv

precaution = pd.read_csv("cleaned_precaution.csv")

print(precaution.head())

precaution_count = precaution.iloc[:, 1:].notnull().sum(axis=1)

plt.figure(figsize=(8,5))
sns.histplot(precaution_count, bins=4)
plt.title("Number of Precautions per Disease")
plt.show()

