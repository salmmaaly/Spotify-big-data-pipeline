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

# Heatmap
plt.figure()
sns.heatmap(df.corr())
plt.savefig("heatmap.png")

# Pairplot
sns.pairplot(df.sample(200))
plt.savefig("pairplot.png")

print("Visualization complete")
os.system(f"python cluster.py {input_path}")