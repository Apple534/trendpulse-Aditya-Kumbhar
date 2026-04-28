import pandas as pd  # pandas import karto / data handle karnyasathi
import matplotlib.pyplot as plt  # charts banvnyasathi
import os  # folder create/check karnyasathi

# -------------------------------
# 🔹 Setup
# -------------------------------

df = pd.read_csv("data/trends_analysed.csv")  
# CSV file load karto ani DataFrame madhe convert karto

os.makedirs("outputs", exist_ok=True)  
# "outputs" folder create karto / already asel tar error nahi


# -------------------------------
# 🔹 Chart 1 — Top 10 Stories by Score
# -------------------------------

top10 = df.sort_values(by="score", ascending=False).head(10)  
# score nusar descending sort karto ani top 10 gheto

top10["short_title"] = top10["title"].str[:60]  
# title shorten karto (first 60 characters)

plt.figure()  
# new chart space create karto

plt.barh(top10["short_title"], top10["score"])  
# horizontal bar chart draw karto

plt.xlabel("Score")  
# x-axis label set karto

plt.ylabel("Title")  
# y-axis label set karto

plt.title("Top 10 Stories by Score")  
# chart title set karto

plt.gca().invert_yaxis()  
# highest score varun top la disnyasathi axis reverse karto

plt.savefig("outputs/chart1_top_stories.png")  
# chart file madhe save karto

plt.show()  
# chart display karto


# -------------------------------
# 🔹 Chart 2 — Stories per Category
# -------------------------------

category_counts = df["category"].value_counts()  
# pratek category madhil stories count karto

plt.figure()  
# new chart create karto

plt.bar(category_counts.index, category_counts.values)  
# bar chart draw karto (categories vs counts)

plt.xlabel("Category")  
# x-axis label

plt.ylabel("Number of Stories")  
# y-axis label

plt.title("Stories per Category")  
# chart title

plt.savefig("outputs/chart2_categories.png")  
# chart save karto

plt.show()  
# display karto


# -------------------------------
# 🔹 Chart 3 — Score vs Comments
# -------------------------------

plt.figure()  
# new chart create karto

plt.scatter(df["score"], df["num_comments"])  
# scatter plot draw karto (x=score, y=comments)

plt.xlabel("Score")  
# x-axis label

plt.ylabel("Number of Comments")  
# y-axis label

plt.title("Score vs Comments")  
# title set karto

plt.savefig("outputs/chart3_scatter.png")  
# chart save karto

plt.show()  
# display karto


# -------------------------------
# 🔹 Bonus — Dashboard
# -------------------------------

fig, axes = plt.subplots(2, 2)  
# 2x2 grid layout create karto (4 charts sathi space)

axes[0, 0].barh(top10["short_title"], top10["score"])  
# first chart (top left) madhe bar chart draw karto

axes[0, 0].set_title("Top 10 Stories")  
# title set karto

axes[0, 0].invert_yaxis()  
# order reverse karto


axes[0, 1].bar(category_counts.index, category_counts.values)  
# second chart (top right) madhe category chart

axes[0, 1].set_title("Stories per Category")  
# title set karto


axes[1, 0].scatter(df["score"], df["num_comments"])  
# third chart (bottom left) scatter plot

axes[1, 0].set_title("Score vs Comments")  
# title set karto


axes[1, 1].axis("off")  
# fourth chart blank thevto (use nahi)


plt.suptitle("TrendPulse Dashboard")  
# full dashboard cha main title

plt.savefig("outputs/dashboard.png")  
# dashboard image save karto

plt.show()  
# dashboard display karto