import pandas as pd
import seaborn as sns
# 1. Read in store_income_task.csv
df=pd.read_csv('store_income_data_task.csv')

# 2. Display the first 5 observations
df.head()
print(df.head())
# 3. Get the number of missing data values per column and print the results
missed_data= df.isnull().sum()
print(missed_data)

countries = pd.read_csv("countries.csv")

countries.head()
sns.histplot(countries['EG.ELC.ACCS.ZS'])

