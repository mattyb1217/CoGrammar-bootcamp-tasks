import pandas as pd

data= {'Name':['a','b','c','d'],
       'Age':[28,32,24,29]}

df=pd.DataFrame(data)
print(df)
mean= df[Age].mean()