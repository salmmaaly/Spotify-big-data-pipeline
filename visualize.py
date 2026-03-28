
import subprocess
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

input_path = sys.argv[1]
df = pd.read_csv(input_path)

# Histogram
plt.figure()
df['pc1'].hist()
plt.title("User Engagement Distribution")
plt.savefig("histogram.png")
plt.show()  # Show the plot in interactive environments
# Heatmap
# Select only numeric columns
numeric_df = df.select_dtypes(include='number') #ashan el heatmap ykon 3ala el numeric features bas msh by2ra el categorical
# Plot correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.savefig("heatmap.png")
plt.show() 


# Scatter plot
plt.figure()
sns.scatterplot(x=df['pc1'], y=df['pc2'])
plt.title("PC1 vs PC2 (User Behavior Clusters)")
plt.savefig("scatter.png")
plt.show()


print("Visualization complete finally!")


#os.system(f"python cluster.py {input_path}")
subprocess.run(["python", "cluster.py", input_path])

