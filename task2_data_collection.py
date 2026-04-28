import pandas as pd  # pandas import karto / data handle karnyasathi vaparto


# -------------------------------
# 🔹 Task 1 — Load JSON
# -------------------------------

file_path = "data/trends_20260427.json"  # JSON file cha path define karto
df = pd.read_json(file_path)  # JSON la DataFrame madhe convert karto

print(f"Loaded {len(df)} stories from {file_path}")  
# kiti rows load zalyat te print karto


# -------------------------------
# 🔹 Task 2 — Clean Data
# -------------------------------

# 1. Duplicates remove karto (same post_id)
df = df.drop_duplicates(subset=["post_id"])  
# same post_id asel tar duplicate rows kadhto

print(f"After removing duplicates: {len(df)}")


# 2. Missing values remove karto
df = df.dropna(subset=["post_id", "title", "score"])  
# jithe post_id/title/score missing ahe te rows kadhto

print(f"After removing nulls: {len(df)}")


# 3. Data types fix karto
df["score"] = pd.to_numeric(df["score"], errors="coerce")  
# score integer madhe convert karto

df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")  
# num_comments integer madhe convert karto


# 4. Low quality remove karto (score < 5)
df = df[df["score"] >= 5]  
# score 5 peksha kami asel tar remove karto

print(f"After removing low scores: {len(df)}")


# 5. Whitespace clean karto
df["title"] = df["title"].str.strip()  
# title madhil extra spaces kadhto


# -------------------------------
# 🔹 Task 3 — Save as CSV
# -------------------------------

output_path = "data/trends_clean.csv"  
# output file path define karto

df.to_csv(output_path, index=False)  
# cleaned data CSV madhe save karto

print(f"Saved {len(df)} rows to {output_path}")


# -------------------------------
# 🔹 Summary
# -------------------------------

print("\nStories per category:")
print(df["category"].value_counts())  
# pratek category madhil story count print karto