## EDA For the symptom_Description.csv

description = pd.read_csv("symptom_Description.csv")

print(description.head())

description["length"] = description["Description"].apply(len)

plt.figure(figsize=(8,5))
sns.histplot(description["length"], bins=10)
plt.title("Distribution of Description Length")
plt.show()