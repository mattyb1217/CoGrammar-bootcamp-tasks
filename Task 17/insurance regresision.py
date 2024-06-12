import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df= pd.read_csv("insurance.csv")
print(df.head())
print(df.describe())
# creating a scatter graph determining how age affects insurance costs

X= df.iloc[:,0].values
y= df.iloc[:,6].values

plt.scatter(X,y, color= 'g')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

# linear regression
X= df.iloc[:,0].values.reshape(-1,1)
y= df.iloc[:,6].values.reshape(-1,1)

LR = LinearRegression()
LR.fit(X,y)

pred= LR.predict(X)
plt.scatter(X,y,color = 'g')
plt.plot(X,pred,color = 'r')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()