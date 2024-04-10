import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df= pd.read_csv('Cars93.csv')
print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.columns)

plt.figure()
sns.boxplot(x= 'Manufacturer', y= 'Rev.per.mile', data= df)
plt.show()

# plt.figure()
# sns.histplot(x= 'MPG.city', data= df)
# plt.show()

# plt.figure()
# sns.histplot(x= 'MPG.highway', data= df)
# plt.show()


# # creating a line plot
# plt.figure()
# sns.lineplot(x= 'Wheelbase', y= 'Turn.circle', data= df)
# plt.show()


# plt.figure()
# sns.histplot(x= 'MPG.city', data= df)
# plt.show()


print(df.groupby('Type')['Horsepower'].mean())

plt.figure()
sns.barplot(x= 'Horsepower',y= 'Type', data= df)
plt.show()

