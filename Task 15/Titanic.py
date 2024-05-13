import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


df =pd.read_csv("Titanic.csv")
print (df.head())
print(df.shape)

print(df.groupby('Pclass')['Survived'].describe())
print(df.columns[:4])

#sns.pairplot(df, hue= 'Survived')
# plt.figure()
# sns.barplot(x= "Survived", y= "Pclass", data =df)
# plt.show()

#corr_matrix= df.iloc[:,:].corr
# Pclass- 1= 1st 2= 2nd 3=3rd
# sibsp- number of siblins/ spouses aboard
# parcg- number of parents/ children aboard
# embarked- c= cherbourg q= queenstown s = southhampton
# survived- 1= yes 0= no

# as there is no lifeboat data in the Titanic.csv data file i have assumed that survial was through the use of lifeboats so will use that data for the secind part against people's class
# need to show what type of people had the most survivors

# plt.figure()
# sns.countplot(y= "Pclass", data =df)
# plt.show()

# plt.xlabel("Pclass")
# plt.title("Count of people in each class")

# need to show sex vs survival to find if more woman survived than men
# find the count of men vs woman

sns.countplot(x="Sex", data =df)
plt.xlabel("Sex")
plt.title("The sex of people on board the Titanic")
plt.show()


