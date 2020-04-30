import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import zipfile 

data=pd.read_csv('GDP growth.csv',error_bad_lines=False)

data=data.iloc[:,:-1]
new_header=data.iloc[0] #making the first row as the header
data=data[1:] #now removing the first row
data.columns=new_header #new column names

df=data.drop(['Indicator Name'],axis=1)
for index,row in df.iterrows():
	val=row['Country Name']
	if 'China' or 'India' in row['Country Name']:
		print(index)
df=df.iloc[:,:-1]
china=df.iloc[38,:]
india=df.iloc[107,:]
china=china[1:]
india=india[1:]

years=[]
for i in range(1961,2019):
	years.append(i)

plt.plot(years,china,label='China')
plt.plot(years,india,label='India')
plt.xlabel('Years(1961-2018)')
plt.ylabel('Annual Growth Rate')
plt.legend()
plt.show()

sum_china=0
for i in china :
	sum_china+=i
avg_china=sum_china/58
print(avg_china)

sum_india=0
for i in india :
	sum_india+=i
avg_india=sum_india/58
print(avg_india)