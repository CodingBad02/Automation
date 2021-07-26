# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:57:16 2021

@author: Sridevi
"""
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import pywhatkit as pwk

#Insert your own personal api_key, check readme.md for more deets

api_key= '7DI40RX0LC805PL8'

ts=TimeSeries(key=api_key,output_format='pandas')
data,meta_data=ts.get_intraday(symbol='AMD',interval='1min',outputsize='full')
print(data)

#Now we explore the closing price and
#Give a Whatsapp alert everytime the Volatitilty exceeds 
#A certain percentage

closure_data=data['4. close']

percentage_change=closure_data.pct_change()

print(percentage_change)
  
#Accessing the last element which is sessentially the latest element of data we need to access

latest_change=percentage_change[-1]

#After analysis, you can suit a best fit for your threshold change, which in turn triggers a whatsapp message
#Directed to a particular number using pywhatkit

thresh_change=0

#For this to run in an infinite loop, we essentially need to give it inside a while loop, please remove
#What you are not using
flag=True
while flag:
    ts=TimeSeries(key=api_key,output_format='pandas')
    data,meta_data=ts.get_intraday(symbol='AMD',interval='1min',outputsize='full')
    closure_data=data['4. close']
    percentage_change=closure_data.pct_change()
    latest_change=percentage_change[-1]
    #Now we begin the intimation case: 
    if abs(latest_change) >= thresh_change:
        pwk.sendwhatmsg_instantly('+919789067642','Hey Manju! The *AMD* stocks seem to be volatile, Have a look and Trade *ASAP*! Note that the Current Percent Change is ' +str(latest_change) ,wait_time= 5,tab_close=True)

#Future: Will try to add a ML pipeline

