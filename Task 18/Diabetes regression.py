import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("diabetes_dirty.csv")
df.head()

df.describe()

df.isnull().sum()

X= df.iloc[:,10].values.reshape(-1,1)
print(X)
y= df.iloc[:,df.columns !='PROGRESSION']
print(y)

X_train, X_test,y_train, y_test= train_test_split(X,y,test_size=0.2, random_state=0)

LR= LinearRegression()
LR.fit(X_train,y_train)
print(X_test)
print(X_train)

print(y_test)
print(y_train)

X_feature= df.drop("PROGRESSION", axis= 1)
y_target= df['PROGRESSION']
y_target

sns.scatterplot(data= X_feature, x= X_feature['PROGRESSION'], y= y_target)

scaler= StandardScaler()
scaler.fit(X_train)

X_train= scaler.transform(X_train)
X_test = scaler.transform(X_test)
X_train

#Mulitple linear regression and predciting X_test
LM= LinearRegression()
model= LM.fit(X_train,y_train)
pred= LM.predict(X_test)
print(pred)

print(LM.intercept_)

print(LM.coef_)

X = df.iloc[:].values
X[:]

y = df.iloc[:,10].values
y = y.reshape(-1, 1)
X = X.reshape(-1, X.shape[1])


multiple = LinearRegression()

multiple.fit(X,y)

print("The intercept is", multiple.intercept_)
print("The coefficeinsts are", multiple.coef_)

print (round (model.score(X_test, y_test), 10))