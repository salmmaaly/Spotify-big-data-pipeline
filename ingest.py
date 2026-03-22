import sys
import pandas as pd
import os


input_path = r"C:\Users\DELL\OneDrive\Desktop\BigData1\spotify_user_behavior_realistic_50000_rows.csv"
df = pd.read_csv(input_path)
print(df.head())


input_path = sys.argv[1]
df = pd.read_csv(input_path)

# basic sanity check
print(df.head())

raw_path = "data_raw.csv"
df.to_csv(raw_path, index=False)

print("Ingestion complete")
os.system(f"python preprocess.py {raw_path}")
