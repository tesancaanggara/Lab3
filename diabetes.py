#
# Diabetes
#

import pandas as pd 

df = pd.read_csv("/Users/hermawansutrisno/Documents/tesanca's/S2/SEMESTER 1/data science/diabetes.csv")

# Add missing values
df2 = df.copy()
df2.loc[2:5, 'Pregnancies'] = None 
df2.head(10)
#print(df2.head(10))

df2.isnull().sum()
df2.shape
df3 = df2.copy()
df3 = df3.dropna()
df3.shape
print(df3.shape)