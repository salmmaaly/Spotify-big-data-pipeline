import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

input_path = sys.argv[1]
df = pd.read_csv(input_path)

# ---- Data Cleaning ----
df.drop_duplicates(inplace=True)
df.fillna(df.median(numeric_only=True), inplace=True)
df.fillna("Unknown", inplace=True)

# ---- Feature Transformation ----
# Convert Yes/No to 1/0
for col in df.columns:
    if df[col].dtype == object and set(df[col].dropna().unique()).issubset({"Yes","No"}):
        df[col] = df[col].map({"Yes":1, "No":0})

# One-hot encode remaining categorical
df = pd.get_dummies(df, drop_first=True)

# Scale numeric
scaler = StandardScaler()
df[df.columns] = scaler.fit_transform(df)

# ---- Dimensionality Reduction ----
pca = PCA(n_components=5)
pca_features = pca.fit_transform(df)

df = pd.DataFrame(pca_features, columns=[f"pc{i}" for i in range(1,6)])

# ---- Discretization ----
df["engagement_level"] = pd.qcut(df["pc1"], q=3, labels=["low","medium","high"])

# Save
output = "data_preprocessed.csv"
df.to_csv(output, index=False)

print("Preprocessing complete")
os.system(f"python analytics.py {output}")
