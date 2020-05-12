import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('gdp_per_capita.csv')
df=df.iloc[:,:-2]
df.columns

our_concern=['Country Name','2018']
data_2018=df[our_concern]

x=data_2018['Country Name']
y=data_2018['2018']


names=[]  #country names
gdp_percapita=[]  #percapita of the countries
y=list(y)
max_val=max(y[1:]) #monaco
index=y.index(max_val)
names.append(x[147])
gdp_percapita.append(max_val)

x=list(x)
val='India'
india=x.index(val)#107
names.append(val)
gdp_percapita.append(y[india])

min_val=min(y[1:]) #
index_min=y.index(min_val)
names.append(x[index_min])
gdp_percapita.append(y[index_min])

max_prop=max(gdp_percapita)/gdp_percapita[1]
print(max_prop) #92.40956904583021

min_prop=gdp_percapita[1]/min(gdp_percapita)
print(min_prop) #7.396370694766739

sns.barplot(names,gdp_percapita)
plt.show()
plt.xlabel('Name of the Countries')
plt.ylabel('Per Capita Income')



























