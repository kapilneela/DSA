import pandas as pd
from sklearn.preprocessing import StandardScaler

file_path = "data.xlsx"  

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

num_cols = df.select_dtypes(include=["number"]).columns
cat_cols = df.select_dtypes(exclude=["number"]).columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

for col in cat_cols:
    df[col] = df[col].astype("category").cat.codes

df[num_cols] = StandardScaler().fit_transform(df[num_cols])

df.to_csv("cleaned_data.csv", index=False)
print("Data preprocessing complete!")
