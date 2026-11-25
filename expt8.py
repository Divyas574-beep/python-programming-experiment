
# EXPERIMENT 8: DATA CLEANING, EDA AND VISUALIZATION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("experiment_8_student_performance.csv")

print("----- ORIGINAL DATASET -----")
print(df.head())

print("\nDataset Shape:", df.shape)

# Missing values and duplicates
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# Data cleaning
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include="object").columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())

for col in cat_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

df.drop_duplicates(inplace=True)

# Calculate average score
df["Average_Score"] = df[["Assignment_Score", "Exam_Score"]].mean(axis=1)

# Classify student performance
df["Performance"] = pd.cut(
    df["Average_Score"],
    bins=[-1, 50, 70, 85, 100],
    labels=["Needs Improvement", "Average", "Good", "Excellent"]
)

print("\n----- CLEANED DATASET -----")
print(df.head(10))

print("\nCleaned Dataset Shape:", df.shape)

# Statistical analysis
print("\n----- STATISTICAL SUMMARY -----")
print(df.describe().round(2))

# Department-wise average exam score
dept_analysis = df.groupby("Department")["Exam_Score"].mean()

print("\n----- DEPARTMENT-WISE AVERAGE -----")
print(dept_analysis.round(2))

# Performance distribution
performance_count = df["Performance"].value_counts()

print("\n----- PERFORMANCE DISTRIBUTION -----")
print(performance_count)

# Graph 1: Department-wise average
dept_analysis.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Department-wise Average Exam Score")
plt.xlabel("Department")
plt.ylabel("Average Exam Score")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Graph 2: Performance distribution
performance_count.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Student Performance Distribution")
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

print("\nData Cleaning and EDA Completed Successfully!")