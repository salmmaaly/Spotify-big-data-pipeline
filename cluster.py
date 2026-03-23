import sys
import pandas as pd
from sklearn.cluster import KMeans
import os

input_path = sys.argv[1]
df = pd.read_csv(input_path)

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['pc1','pc2','pc3']])

counts = df['cluster'].value_counts()

with open("clusters.txt","w") as f:
    f.write("Cluster distribution:\n")
    f.write(str(counts))

print("Clustering complete")