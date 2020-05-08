import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('GDP growth.csv')
new_cols=data.iloc[0,:]
data=data.iloc[1:,:]
data.columns=new_cols

data=data.iloc[:,:-2]
x=0
for index,row in data.iterrows():
	val=row['Country Name']
	if val=='Japan':
		#print(index)  #here this index starts from 1 so the posn is 117 and not 118
		x=index-1
df_japan=data.iloc[x,:]
df_japan=df_japan.reset_index(drop=True)
df_japan=df_japan.drop(1)
df_japan=df_japan.drop(0)
years=[]
for i in range(1961,2019):
	years.append(i)
mark=[]
for i in range(len(df_japan)):
	if df_japan[i]<0:
		mark.append(i)
print(mark)
#unik=[]	
df_japan=df_japan.reset_index(drop=True)
#print(unik)

plt.plot(years,df_japan,label='-ve growth rate',markevery=mark,marker='o',color='orange')
plt.title('Visualising Data')
plt.xlabel('Years')
plt.ylabel('Growth Rate %')
plt.legend()
plt.show()



















