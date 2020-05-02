import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('countrywise_airline_rescheduling.csv')
india=df[13:14]
world=df[0:1]
japan=df[15:16]
usa=df[12:13]
china=df[14:15]
world=world.drop(['Countries'],axis=1)	
china=china.drop(['Countries'],axis=1)	
usa=usa.drop(['Countries'],axis=1)	
india=india.drop(['Countries'],axis=1)	
japan=japan.drop(['Countries'],axis=1)	

col=world.columns

india=india.reset_index(drop=True)
ind=india.iloc[0,:]
ind=ind.reset_index(drop=True)
ind=ind[1:]
ind=ind.reset_index(drop=True)

chn=china.reset_index(drop=True)
chn=chn.iloc[0,:]  
chn=chn.reset_index(drop=True)


us=usa.reset_index(drop=True)
us=us.iloc[0,:]
us=us.reset_index(drop=True)


wor=world.reset_index(drop=True)
wor=wor.iloc[0,:]
wor=wor.reset_index(drop=True)

for i in range(len(ind)):
	if "%" in ind[i]:
		val=ind[i]
		val=val[:-1]
		val=float(val)
		ind[i]=val

for i in range(len(chn)):
	if "%" in chn[i]:
		val=chn[i]
		val=val[:-1]
		val=float(val)
		chn[i]=val
		
for i in range(len(us)):
	if "%" in us[i]:
		val=us[i]
		val=val[:-1]
		val=float(val)
		us[i]=val

for i in range(len(wor)):
	if "%" in wor[i]:
		val=wor[i]
		val=val[:-1]
		val=float(val)
		wor[i]=val
		
plt.plot(col,ind,label='India')
plt.plot(col,us,label='USA')
plt.plot(col,wor,label='World')
plt.plot(col,chn,label='China')
plt.legend()	
plt.xticks(rotation=45)
plt.xlabel('Dates(as metrics)')
plt.ylabel('Percentage of Flight Re-Scheduling')
plt.title('Impact of Covid on Flight Reservation')
plt.show()	




			