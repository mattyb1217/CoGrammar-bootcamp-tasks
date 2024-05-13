import fuzzywuzzy
from fuzzywuzzy import process
import chardet
import fuzzywuzzy.fuzz
import fuzzywuzzy.process
import pandas as pd

df= pd.read_csv('store_income_data_example.csv')
print(df.head())

unique_countries= df['country'].unique()
print(unique_countries)

print(f"there is {len(unique_countries)} unique countries")
unique_countries

#lower case countries
df['country']= df['country'].str.lower()
print(df['country'])

df['country']= df['country'].str.strip()
print(df['country'])

unique_countries = df['country'].unique()
print(f"there is {len(unique_countries)} unique countries")


names= fuzzywuzzy.process.extract('uk', unique_countries, limit= 10, scorer= fuzzywuzzy.fuzz.token_set_ratio)


print(df.head())

df.replace("uk","United Kingdom", inplace=True)
df.replace("uk/","United Kingdom",inplace=True)
df.replace("uk.","United Kingdom",inplace=True)
df.replace("united kingdom","United Kingdom",inplace=True)
df.replace("united kingdom.","United Kingdom",inplace=True)
df.replace("united kingdom/","United Kingdom",inplace=True)

df.replace("united states of america.","United States",inplace=True)
df.replace("united states of america","United States",inplace=True)
df.replace("united states of america/","United States",inplace=True)
df.replace("united states","United States", inplace=True)
df.replace("united states.","United States", inplace=True)
df.replace("united states/","United States", inplace=True)

df.replace("south africa","South Africa",inplace=True)
df.replace("south africa/","South Africa",inplace=True)
df.replace("south africa.","South Africa",inplace=True)

df["country"].unique()

from datetime import date
df.head()
df['days_ago']= pd.to_datetime(df['date_measured'], format = '%d %B %Y')
df['days_ago'].head()