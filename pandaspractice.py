#
# Tesanca Anggara
# Pandas practice 
#

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/hermawansutrisno/Documents/tesanca's/smoker.csv")

# Inspect structure
df.shape
df.info()

df.head()
df.tail()

# Inspect value
df.head()
df.tail()

# Visualize
df['smoker'].hist()
plt.show()

# Sum
df.sum()
print(df.sum(axis=1))