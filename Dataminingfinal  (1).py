!pip install rapidfuzz

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from rapidfuzz import process


df = pd.read_csv("cleaned_dataset.csv")
description_df = pd.read_csv("symptom_Description.csv")
precaution_df = pd.read_csv("cleaned_precaution.csv")
severity_df = pd.read_csv("Symptom-severity.csv")

symptom_columns = df.drop("Disease", axis=1).columns

# Clean symptoms
for col in symptom_columns:
    df[col] = df[col].astype(str).str.strip()

df["Disease"] = df["Disease"].astype(str).str.strip()

# Clean severity file
severity_df["Symptom"] = severity_df["Symptom"].astype(str).str.strip()
severity_dict = dict(zip(severity_df["Symptom"], severity_df["weight"]))


unique_symptoms = pd.unique(df[symptom_columns].values.ravel())
unique_symptoms = [s for s in unique_symptoms if s != "nan"]

X = pd.DataFrame(0, index=df.index, columns=unique_symptoms)

for i in range(len(df)):
    for symptom in df.loc[i, symptom_columns]:
        if symptom != "nan":
            weight = severity_dict.get(symptom, 1)
            scaled_value = 1 + (weight * 0.2)
            X.loc[i, symptom] = scaled_value

X.columns = X.columns.astype(str).str.strip()
y = df["Disease"]

unique_symptoms = pd.unique(df[symptom_columns].values.ravel())
unique_symptoms = [s for s in unique_symptoms if s != "nan"]

X = pd.DataFrame(0, index=df.index, columns=unique_symptoms)

for i in range(len(df)):
    for symptom in df.loc[i, symptom_columns]:
        if symptom != "nan":
            weight = severity_dict.get(symptom, 1)
            scaled_value = 1 + (weight * 0.2)
            X.loc[i, symptom] = scaled_value

X.columns = X.columns.astype(str).str.strip()
y = df["Disease"]

def create_input_vector(symptoms):

    input_df = pd.DataFrame(0, index=[0], columns=X.columns)

    for user_symptom in symptoms:
        user_symptom = user_symptom.strip().lower()

        match, score, _ = process.extractOne(user_symptom, X.columns)

        if score >= 80:
            weight = severity_dict.get(match, 1)
            scaled_value = 1 + (weight * 0.2)
            input_df.at[0, match] = scaled_value

    return input_df

def show_all_probabilities(symptoms):

    input_df = create_input_vector(symptoms)

    probabilities = model.predict_proba(input_df)[0]
    diseases = model.classes_

    results = sorted(
        zip(diseases, probabilities),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n--- Disease Probabilities ---\n")

    for disease, prob in results:
        print(f"{disease} → {round(prob*100,2)}%")

    return results


def interactive_diagnosis():

    symptoms = []

    print("\nEnter patient symptoms (type 'done' when finished):")

    while True:
        symptom = input("Enter symptom: ").strip()

        if symptom.lower() == "done":
            break

        symptoms.append(symptom)

        results = show_all_probabilities(symptoms)

        best_disease, best_prob = results[0]

        if best_prob >= 0.70:
            print("\n✅ High confidence diagnosis reached.")
            break
        else:
            print("\n⚠ Confidence low. Please add more symptoms.")

    print("\n==============================")
    print("Final Predicted Disease:", best_disease)
    print("Confidence:", round(best_prob*100,2), "%")

    # Description
    desc = description_df[
        description_df["Disease"].str.strip() == best_disease
    ]["Description"].values

    if len(desc) > 0:
        print("\nDescription:")
        print(desc[0])

    # Precautions
    prec = precaution_df[
        precaution_df["Disease"].str.strip() == best_disease
    ]

    if not prec.empty:
        print("\nPrecautions:")
        for p in prec.iloc[0, 1:]:
            if pd.notna(p) and p != "No precaution available":
                print("-", p)


interactive_diagnosis()


