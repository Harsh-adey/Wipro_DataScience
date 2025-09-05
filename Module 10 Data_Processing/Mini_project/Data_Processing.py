import pandas as pd

df=pd.read_csv("melb_data.csv")
print(df)
print(df.shape)
print(df.info())
print(df.describe())
col=list(df.columns)
print(col)

print(df.isnull().sum()) # missing values

df['Distance'].fillna(df['Distance'].median(), inplace=True)
df['Postcode'].fillna(df['Postcode'].mode()[0], inplace=True)
df['Regionname'].fillna(df['Regionname'].mode()[0], inplace=True)
df['Propertycount'].fillna(df['Propertycount'].median(), inplace=True)


df['Bedroom2'].fillna(df['Bedroom2'].median(), inplace=True)
df['Bathroom'].fillna(df['Bathroom'].median(), inplace=True)
df['Car'].fillna(df['Car'].median(), inplace=True)

# using mode for categorical data
df['CouncilArea'].fillna(df['CouncilArea'].mode()[0], inplace=True)

df['Lattitude'].fillna(df['Lattitude'].median(), inplace=True)
df['Longtitude'].fillna(df['Longtitude'].median(), inplace=True)

# dropping the highest missing values columns
df.drop(columns=['BuildingArea', 'YearBuilt'], inplace=True)

df['Landsize'].fillna(df['Landsize'].median(), inplace=True)

print(df.isnull().sum()) # verifying again
