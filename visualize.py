
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


# Pairplot
print("Creating pairplot...")

try:
    sample_df = df.sample(100)

    pairplot = sns.pairplot(sample_df)
    pairplot.fig.suptitle("Pairplot of Features", y=1.02)  # optional title

    pairplot.savefig("C:/Users/DELL/OneDrive/Desktop/BigData1/pairplot.png")

    print("Pairplot saved successfully")
    plt.show() 
    

except Exception as e:
    print("Error in pairplot:", e)

print("Visualization complete")


#os.system(f"python cluster.py {input_path}")
subprocess.run(["python", "cluster.py", input_path])

