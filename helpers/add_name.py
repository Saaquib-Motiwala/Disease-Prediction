# import pandas as pd
#
# df = pd.read_csv('Symptom-severity.csv')
#
# df["Name"] = df["Symptom"].replace("_", " ", regex=True)
# df["Name"] = df["Name"].str.capitalize()
#
# df.to_csv("Symptom-severity-updated.csv")

# import pandas as pd
#
# df = pd.read_csv('Symptom-severity-updated.csv')
#
# print(list(df["Name"].sort_values()))