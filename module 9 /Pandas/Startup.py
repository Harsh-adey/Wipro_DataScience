"""Exercise 4 :  Download startups dataset                                                                                                                           Link  : https://www.kaggle.com/datasets/farhanmd29/50-startups  
a.  Create DataFrame using Pandas
b.  Read the data from startups.csv file and load the data into dataframe.
c.  Check the statistical summary.
d. Check for corelation coefficient between dependent and independent variables."""


import pandas as pd

# a.  Create DataFrame using Pandas

data=pd.read_csv("Startups.csv")

# b.  Read the data from 50_startups.csv file and load the data into dataframe.

df=pd.DataFrame(data.head(50))
print(df)

# c.  Check the statistical summary.

print(df.describe())

# d. Check for corelation coefficient between dependent and independent variables.

print(df.corr(numeric_only=True))
print("\nCorrelation of mpg with other variables:")
print(df.corr(numeric_only=True)['Profit'])
