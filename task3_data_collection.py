import pandas as pd  # data handle karnyasathi
import numpy as np   # numerical analysis sathi

# -------------------------------
# 🔹 Task 1 — Load and Explore
# -------------------------------

file_path = "data/trends_clean.csv"  # cleaned CSV file path
df = pd.read_csv(file_path)  # CSV load karto

print(f"Loaded data: {df.shape}")  # (rows, columns)

print("\nFirst 5 rows:")
print(df.head())  # first 5 rows print karto


# Average score and comments
avg_score = df["score"].mean()  # average score
avg_comments = df["num_comments"].mean()  # average comments

print(f"\nAverage score: {int(avg_score)}")
print(f"Average comments: {int(avg_comments)}")


# -------------------------------
# 🔹 Task 2 — NumPy Analysis
# -------------------------------

scores = df["score"].values  # numpy array madhe convert karto

print("\n--- NumPy Stats ---")

print(f"Mean score: {int(np.mean(scores))}")  
print(f"Median score: {int(np.median(scores))}")  
print(f"Std deviation: {int(np.std(scores))}")  

print(f"Max score: {int(np.max(scores))}")  
print(f"Min score: {int(np.min(scores))}")  


# Category with most stories
top_category = df["category"].value_counts().idxmax()
top_count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")


# Story with most comments
max_comment_row = df.loc[df["num_comments"].idxmax()]

print(f'\nMost commented story: "{max_comment_row["title"]}" — {int(max_comment_row["num_comments"])} comments')


# -------------------------------
# 🔹 Task 3 — Add New Columns
# -------------------------------

# engagement = num_comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)  
# division by zero avoid karnyasathi +1

# is_popular = True if score > average_score else False
df["is_popular"] = df["score"] > avg_score  


# -------------------------------
# 🔹 Task 4 — Save Result
# -------------------------------

output_path = "data/trends_analysed.csv"  

df.to_csv(output_path, index=False)  

print(f"\nSaved to {output_path}")