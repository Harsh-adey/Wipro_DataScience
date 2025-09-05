# 1. Perform  Data Preprocessing  on melb_data.csv dataset with statistical perspective. The dataset can be downloaded from   https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


df = pd.read_csv("DataProcessing.csv")
print("Shape before preprocessing:", df.shape)

if 'Address' in df.columns:
    df.drop(columns=['Address'], inplace=True)
if 'Date' in df.columns:
    df.drop(columns=['Date'], inplace=True)


X = df.drop("Price", axis=1)
y = df["Price"]


numeric_features = X.select_dtypes(include=[np.number]).columns
categorical_features = X.select_dtypes(exclude=[np.number]).columns

print("Numeric Features:", list(numeric_features))
print("Categorical Features:", list(categorical_features))

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


X_processed = preprocessor.fit_transform(X)
print("Shape after preprocessing:", X_processed.shape)

X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)


# 2. Perform  Data Preprocessing  on   melb_data.csv dataset with statistical perspective. The dataset can be downloaded from   https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download

import pandas as pd
import numpy as np


df = pd.read_csv("DataProcessing.csv")
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())


print("\nDataset Info:")
print(df.info())

print("\nMissing values count:\n", df.isnull().sum())


missing_percent = (df.isnull().sum() / len(df)) * 100
print("\nMissing Values (%):\n", missing_percent[missing_percent > 0])


num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)


cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing values after imputation:", df.isnull().sum().sum())


if 'Address' in df.columns:
    df.drop(columns=['Address'], inplace=True)
if 'Date' in df.columns:
    df.drop(columns=['Date'], inplace=True)

print("\nShape after dropping irrelevant columns:", df.shape)


df = pd.get_dummies(df, drop_first=True)
print("\nShape after encoding:", df.shape)


print("\nStatistical Summary:\n", df.describe())


print("\nSkewness of numerical features:\n", df.skew())


numeric_df = df.select_dtypes(include=[np.number])

Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).sum()
print("\nOutlier count per numeric column:\n", outliers)
