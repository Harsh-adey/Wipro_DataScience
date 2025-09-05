# 1.  Perform Exploratory Data Analysis for the dataset Mall_Customers. The dataset can be downloaded from  https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("Mall_Customers.csv")
print("First 5 rows:")
print(df.head())




print("\nDataset Info:")
print(df.info())


print("\nMissing values:")
print(df.isnull().sum())


plt.figure(figsize=(14,4))

plt.subplot(1,3,1)
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution')

plt.subplot(1,3,2)
sns.histplot(df['Annual Income (k$)'], bins=20, kde=True, color='orange')
plt.title('Annual Income Distribution')

plt.subplot(1,3,3)
sns.histplot(df['Spending Score (1-100)'], bins=20, kde=True, color='green')
plt.title('Spending Score Distribution')

plt.tight_layout()
plt.show()


plt.figure(figsize=(5,4))
sns.countplot(x='Gender', data=df, palette='Set2')
plt.title('Gender Distribution')
plt.show()


plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Gender', data=df, palette='husl')
plt.title('Age vs Spending Score by Gender')
plt.show()


plt.figure(figsize=(6,4))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', data=df, palette='Set1')
plt.title('Income vs Spending Score by Gender')
plt.show()


plt.figure(figsize=(14,4))

plt.subplot(1,3,1)
sns.boxplot(x='Gender', y='Age', data=df, palette='pastel')
plt.title('Age by Gender')

plt.subplot(1,3,2)
sns.boxplot(x='Gender', y='Annual Income (k$)', data=df, palette='pastel')
plt.title('Annual Income by Gender')

plt.subplot(1,3,3)
sns.boxplot(x='Gender', y='Spending Score (1-100)', data=df, palette='pastel')
plt.title('Spending Score by Gender')

plt.tight_layout()
plt.show()


plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# 2. Perform Exploratory Data Analysis for the dataset  salary_data. The dataset can be downloaded from  https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("Salary_Data.csv")
print("First 5 rows:")
print(df.head())



print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())



plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
sns.histplot(df['YearsExperience'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Years of Experience')

plt.subplot(1,2,2)
sns.histplot(df['Salary'], bins=10, kde=True, color='orange')
plt.title('Distribution of Salary')

plt.tight_layout()
plt.show()


plt.figure(figsize=(6,4))
sns.scatterplot(x='YearsExperience', y='Salary', data=df, color='green')
plt.title('Years of Experience vs Salary')
plt.show()


plt.figure(figsize=(6,4))
sns.regplot(x='YearsExperience', y='Salary', data=df, ci=None, line_kws={"color":"red"})
plt.title('Regression Line: Experience vs Salary')
plt.show()


plt.figure(figsize=(4,3))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# Perform Exploratory Data Analysis for the dataset  Social Network Ads. The dataset can be downloaded from  https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("Social_Network_Ads.csv")
print("First 5 rows:")
print(df.head())



print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe(include='all'))


df = df.drop(columns=['User ID'])

-

plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
plt.title('Age Distribution')

plt.subplot(1,2,2)
sns.histplot(df['EstimatedSalary'], bins=15, kde=True, color='orange')
plt.title('Estimated Salary Distribution')

plt.tight_layout()
plt.show()


plt.figure(figsize=(5,4))
sns.countplot(x='Gender', data=df, palette='Set2')
plt.title('Gender Distribution')
plt.show()


plt.figure(figsize=(5,4))
sns.countplot(x='Purchased', data=df, palette='husl')
plt.title('Purchased Distribution')
plt.show()


plt.figure(figsize=(6,4))
sns.boxplot(x='Purchased', y='Age', data=df, palette='Set1')
plt.title('Age vs Purchased')
plt.show()


plt.figure(figsize=(6,4))
sns.boxplot(x='Purchased', y='EstimatedSalary', data=df, palette='Set3')
plt.title('Estimated Salary vs Purchased')
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='EstimatedSalary', hue='Purchased', style='Gender', data=df, palette='husl')
plt.title('Age vs Estimated Salary (by Purchased & Gender)')
plt.show()


plt.figure(figsize=(5,3))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
