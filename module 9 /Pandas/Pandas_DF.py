# Pandas-DataFrame 
""" Exercise 3: Pandas-DataFrame
Download the data set and rename to cars.csv
Link : Dataset: https://www.kaggle.com/uciml/autompg-dataset/data?select=auto-mpg.csv
 or
https://archive.ics.uci.edu/ml/datasets/Auto+MPG

   a. Import Pandas
   b. Import the Cars Dataset and store the Pandas DataFrame in the variable cars
   c. Inspect the first 10 Rows of the DataFrame cars
   d. Inspect the DataFrame cars by "printing" cars
   e. Inspect the last 5 Rows
   f. Get some meta information on our DataFrame! """

# a. Import Pandas

import pandas as pd

#  b. Import the Cars Dataset and store the Pandas DataFrame in the variable cars

df=pd.read_csv("Cars.csv")

# c. Inspect the first 10 Rows of the DataFrame cars

print(df.head(10))

#  d. Inspect the DataFrame cars by "printing" cars

print(df.columns)
print(df["car name"]) # for printing  whole column 
print(df["car name"].unique()) # for printing different elements in column
print(df["car name"].value_counts()) # for counting the no of times a element appears
print(df["car name"].describe())

#  e. Inspect the last 5 Rows

print(df.tail(5))

#  f. Get some meta information on our DataFrame!

print(df.info())
