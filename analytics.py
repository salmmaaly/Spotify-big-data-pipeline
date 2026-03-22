import sys
import pandas as pd
import os

input_path = sys.argv[1]
df = pd.read_csv(input_path)

# Insight 1
with open("insight1.txt","w") as f:
    f.write(f"Most users fall into engagement group: {df['engagement_level'].value_counts().idxmax()}")

# Insight 2
with open("insight2.txt","w") as f:
    f.write(f"Average PC1 (engagement proxy): {df['pc1'].mean():.2f}")

# Insight 3
with open("insight3.txt","w") as f:
    f.write(f"Variance in behavior (PC2 std): {df['pc2'].std():.2f}")

print("Analytics complete")
os.system(f"python visualize.py {input_path}")
