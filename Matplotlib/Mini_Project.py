import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("diabetes.csv")
print("First 5 rows:")
print(df.head())


print("\nMissing values:")
print(df.isnull().sum())


columns_with_zero_missing = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for col in columns_with_zero_missing:
    df[col].replace(0, np.nan, inplace=True)

print("\nMissing values after replacing 0 with NaN:")
print(df.isnull().sum())


for col in columns_with_zero_missing:
    df[col].fillna(df[col].median(), inplace=True)

print("\nClass distribution:")
print(df['Outcome'].value_counts())


plt.figure(figsize=(12,8))
for i, col in enumerate(df.columns, 1):
    plt.subplot(3,3,i)
    sns.histplot(df[col], bins=20, kde=True, color="skyblue")
    plt.title(f"Distribution of {col}")
plt.tight_layout()
plt.show()


plt.figure(figsize=(12,6))
sns.boxplot(data=df, orient="h", palette="Set2")
plt.title("Boxplot for Outlier Detection")
plt.show()


plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


plt.figure(figsize=(12,10))
for i, col in enumerate(df.columns[:-1], 1):
    plt.subplot(3,3,i)
    sns.boxplot(x="Outcome", y=col, data=df, palette="Set1")
    plt.title(f"{col} vs Outcome")
plt.tight_layout()
plt.show()


sns.pairplot(df, hue="Outcome", diag_kind="kde", palette="husl")
plt.show()
