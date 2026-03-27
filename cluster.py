import sys
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

input_path = sys.argv[1]
df = pd.read_csv(input_path)

# Fit KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['pc1','pc2','pc3']])

# Save cluster distribution
counts = df['cluster'].value_counts()
with open("clusters.txt","w") as f:
    f.write("Cluster distribution:\n")
    f.write(str(counts))

# Save a non-blocking cluster plot
plt.figure(figsize=(8,6))
plt.scatter(df['pc1'], df['pc2'], c=df['cluster'], cmap='viridis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('KMeans Clusters')
plt.savefig("cluster_plot.png")
plt.show() 
plt.close()   # <-- prevents blocking in Docker/pipeline

print("Clustering complete")