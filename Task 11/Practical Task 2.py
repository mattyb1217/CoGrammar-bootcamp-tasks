import pandas as pd

df= pd.read_csv('balance.txt', sep= ' ')

print (df.head())
print(df.columns)


# Comparing the average income based on ethnicity
print(df.groupby('Ethnicity')['Income'].mean())

# Comparing the average balance based on marriage status
print(df.groupby('Married')['Balance'].mean())

#Finding the highest income of the dataset
print(df.Income.max())

#Finding the lowest income of the dataset
print(df.Income.min())

#Finding the amount of cards recorded in the dataset
print(df.Cards.sum())



print(df.Gender == 'Female')
print(df.Gender == 'Male')

print(df.Gender.count())

