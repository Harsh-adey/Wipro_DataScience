import numpy as np
import pandas as pd

df = pd.read_csv("datasetExample.csv")

def outlier_detection(df):
    outliers = {}
    numeric_df = df.select_dtypes(include=[np.number])
    for col in numeric_df.columns:
        data = numeric_df[col].dropna() 
        q1, q3 = np.percentile(data, [25, 75])
        IQR = q3 - q1
        lr = q1 - 1.5 * IQR
        ur = q3 + 1.5 * IQR
        
       
        col_outliers = data[(data < lr) | (data > ur)]
        outliers[col] = col_outliers.values
    
    return outliers


outliers = outlier_detection(df)
print(outliers)
