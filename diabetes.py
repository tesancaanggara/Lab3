#
# Diabetes
# Tesanca Anggara
#

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/hermawansutrisno/Documents/tesanca's/S2/SEMESTER 1/data science/diabetes.csv")

# Add missing values 1
df2 = df.copy()
df2.loc[2:5, 'Pregnancies'] = None 
df2.head(10)
#print(df2.head(10))

# Add missing values 2
df2.isnull().sum()
df2.shape
df3 = df2.copy()
df3 = df3.dropna()
df3.shape
#print(df3.shape)

# Creating new columns based on other columns
df2['Glucose_Insulin_Ratio'] = df2['Glucose']/df2['Insulin']
#print(df2.head(5))

# Count by values
df['Outcome'].value_counts()
df['Outcome'].value_counts(normalize = True)
df.groupby('Outcome').mean()
#print(df.groupby('Outcome').mean())

# By group
df.groupby(['Pregnancies', 'Outcome']).mean()
#print(df.groupby(['Pregnancies', 'Outcome']).mean())

# Chart
df[['BMI', 'Glucose']].plot.line(figsize = (10, 5),
                                  color = {"BMI": "red", "Glucose": "blue"})
plt.title('Tesanca Anggara')
plt.show()