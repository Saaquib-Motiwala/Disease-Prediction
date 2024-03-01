import pandas as pd
import numpy as np
import joblib


def predictor(user_symptoms):
    user_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # df1 = pd.read_csv('../dataset/Symptom-severity-updated.csv')
    df1 = pd.read_csv('../Symptom-severity-updated.csv')
    description = pd.read_csv("../datasets/symptom_Description.csv")
    precaution = pd.read_csv("../datasets/symptom_precaution.csv")
    loaded_rf = joblib.load("random_forest_new.joblib")

    count = 0
    for i in user_symptoms:
        for j in range(len(df1)):
            if i == df1["Name"][j]:
                user_list[count] = (df1["Symptom"][j])
                count += 1

    symptoms = user_list
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    for j in range(len(symptoms)):
        for k in range(len(a)):
            if symptoms[j] == a[k]:
                symptoms[j] = b[k]

    symptoms = [symptoms]
    pred = loaded_rf.predict(symptoms)

    descr = description[description['Disease'] == pred[0]]
    descr = descr.values[0][1]

    c = np.where(precaution['Disease'] == pred[0])[0][0]
    precaution_list = []
    for i in range(1, len(precaution.iloc[c])):
        precaution_list.append(precaution.iloc[c, i])

    prediction_info = [pred[0], descr, precaution_list]
    return prediction_info


if __name__ == '__main__':
    predictor([""])
