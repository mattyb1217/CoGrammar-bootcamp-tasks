import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df=pd.read_csv('diabetes_updated.csv')
df.head()
print(df.describe())

# X= df.iloc[:,8].values.reshape(-1,1)
# #print(X)
# y= df.iloc[:,df.columns !='Outcome']
# #print(y)


# # creating train and test sets
# #80% train, 20% test

# X_train, X_test,y_train, y_test= train_test_split(X,y,test_size=0.2, random_state=0)

# LR= LinearRegression()
# LR.fit(X_train,y_train)


# print(X_test)
# print(X_train)

# print(y_test)
# print(y_train)

X_feature= df.drop("Outcome", axis= 1)
y_target= df['Outcome']

#multiple regression

x= df.iloc[:,[0,1,2,3,4,5,6,7]]
print(x[0:4])