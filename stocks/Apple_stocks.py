import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_appl=pd.read_csv('nasdaq_aapl_6months.csv')
x_train=df_appl['Date']
y_train=df_appl[' Close/Last']
price=[]
#will store 
for i in y_train:
	#print(i)
	i=i.replace('$','')
	price.append(float(i))
print(price)
#type(price[2])
max_price=max(price)
min_price=min(price)
dev=(max_price-min_price)/124
#print(dev)

dates=[]
import datetime
import time
for i in x_train:
	val=time.mktime(datetime.datetime.strptime(i,'%m/%d/%Y').timetuple())
	dates.append(val)
#print(dates)
	
plt.plot(dates,price,label='Apple')
plt.xlabel('Dates in Time Stamp')
plt.ylabel('Stock Price')
plt.title('Stock Price Trends')
plt.legend()
plt.show()

print(np.shape(dates))
dates=np.reshape(dates,(124,1))

#svm
from sklearn.svm import SVR
regressor=SVR(kernel='rbf',C=20)
regressor.fit(dates,price)
score_svm=regressor.score(dates,price)
print(score_svm)

#predicting the value : svm 
new_date='05/01/2020'
unixtime=time.mktime(datetime.datetime.strptime(new_date,'%m/%d/%Y').timetuple())
unixtime=np.reshape(unixtime,(1,-1))
y_pred=regressor.predict(unixtime)
print(y_pred)

#printing the max and min stock prices in this tenure of 6 months
record=[]
for index,row in df_appl.iterrows():
	val=row['Date']
	if f'${max_price}' in row[' Close/Last']:
		record.append(val)
	elif f'${min_price}' in row[' Close/Last']:
		record.append(val) 
	
print('Max has been :',max_price,' On :',record[0])
print('Min has been :',min_price,' On :',record[1])

#linear regression
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(dates,price)
score_lr=lr.score(dates,price)

