import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("customers.csv")

# Display first 5 rows
print("===== FIRST 5 ROWS =====")
print(df.head())

# Display dataset shape
print("\n===== DATASET SHAPE =====")
print(df.shape)

# Display column names
print("\n===== COLUMN NAMES =====")
print(df.columns)

# Display dataset information
print("\n===== DATASET INFORMATION =====")
df.info()

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Check duplicate rows
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# Statistical summary
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())
import os

# Create visualizations folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

import os

# Create visualizations folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# Generate Income Distribution Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df["annual_income_k"], bins=20, kde=True, color="skyblue")
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Number of Customers")
plt.tight_layout()

# Save image to visualizations folder
plt.savefig("visualizations/income_distribution.png")
plt.show()


# Generate Spending Score Distribution Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df["spending_score"], bins=20, kde=True, color="salmon")
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Number of Customers")
plt.tight_layout()

# Save image to visualizations folder
plt.savefig("visualizations/spending_distribution.png")
plt.show()

# Generate Annual Income vs Spending Score Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, 
    x="annual_income_k", 
    y="spending_score", 
    color="purple", 
    alpha=0.7
)
plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Save image to visualizations folder
plt.savefig("visualizations/income_vs_spending.png")
plt.show()