import pandas as pd

df=pd.read_csv('balance.txt',sep=' ')
   # "sep=' ' " needed to seperate headings and table up - space needed in the '' to not get an error

#print (df.head())
# # print(df.tail())
# # print(df.shape)
# # print(df.info())
# # print(df.describe())
# # print(df.columns)


# first_5_of_limit= df[['Limit', 'Rating']]
# print(first_5_of_limit.sample(5))


# print(df.iloc[:5,2]) # limit
# print(df.iloc[:5,3]) # Rating

first_5_of_limit= df["Limit"]
print(first_5_of_limit.head())

first_5_of_Rating= df["Rating"]
print(first_5_of_Rating.head())


# first 5 with 4 cards

four_cards= df["Cards"]
print(df[df.Cards == 4])

print(df.sort_values(by='Education', ascending=False),)