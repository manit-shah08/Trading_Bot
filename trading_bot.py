from fyers_api import fyersModel
from fyers_api import accessToken
from pandas import DataFrame
import pandas as pd
import time as t
from datetime import date
import talib
import numpy
import yfinance as yf

pip install fyers-apiv2

client_id = 'LW2A574KDQ-xxx'
secret_key = 'T5PI7Rxxxx'
redirect_uri = 'https://127.0.0.1:5000/'

session=accessToken.SessionModel(client_id=client_id,
secret_key=secret_key,redirect_uri=redirect_uri, 
response_type='code', grant_type= "authorization_code")

response = session.generate_authcode()
response

auth_code = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2MzQ0OTg5ODEsImV4cCI6MTYzNDQ5OTI4MSwibmJmIjoxNjM0NDk4OTgxLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUDEwODQ4Iiwibm9uY2UiOiIiLCJhcHBfaWQiOiJMVzJBNTc0S0RRIiwidXVpZCI6IjVkY2JjN2MzZjZkNTQwYTBiYjQ0MjRjMGZiNjIwMmRkIiwiaXBBZGRyIjoiNDMuMjUwLjE1OC4xNzQiLCJzY29wZSI6IiJ9.i2ZzRz7f9_n5lx1UlstOHjZokXt189j_Qqy6EMOyaHM'

session.set_token(auth_code)
response = session.generate_token()
access_token = response["access_token"]

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)

fyers.get_profile()

fyers.funds()

filename = r'ind_nifty500list (2).xlsx'
df = pd.read_excel(filename)

symbol = []
symbol = list(df['Symbol'])
print(symbol)
print(len(symbol))

today = date.today()
d1 = today.strftime("%Y-%m-%d")
print("d1 =", d1)

#df = None
df = pd.DataFrame(columns=['o','h','l','c','symbol'])
df

import thread
import time

def db_pt1():
    for i in symbol[0:200]:
        
        try:
            data1 = {"symbol":i,"resolution":"D","date_format":"1","range_from":"2021-10-14","range_to":"2021-10-14","cont_flag":"1"}
            f = fyers.history(data1)
            
            sliced_list = f['candles']
            sliced_list = sliced_list[0]
            sliced_list = sliced_list[1:5]
            sliced_list.append(i)
            print(sliced_list)
            
            
            df.loc[len(df), :] = sliced_list
        except:
        
            print("Error in ",i)


def db_pt2():
    for i in symbol[200:400]:
        try:
            data1 = {"symbol":i,"resolution":"D","date_format":"1","range_from":"2021-10-14","range_to":"2021-10-14","cont_flag":"1"}
            f = fyers.history(data1)
            
            sliced_list = f['candles']
            sliced_list = sliced_list[0]
            sliced_list = sliced_list[1:5]
            sliced_list.append(i)
            print(sliced_list)
            df.loc[len(df), :] = sliced_list
        
        except: 
            print("Error in ",i)

def db_pt3():
    for i in symbol[400:501]:
        try:
            data1 = {"symbol":i,"resolution":"D","date_format":"1","range_from":"2021-10-14","range_to":"2021-10-14","cont_flag":"1"}
            f = fyers.history(data1)
            
            sliced_list = f['candles']
            sliced_list = sliced_list[0]
            sliced_list = sliced_list[1:5]
            sliced_list.append(i)
            print(sliced_list)
            
            df.loc[len(df), :] = sliced_list
        
        except: 
            print("Error in ",i)



db_pt1()
df

db_pt2()
df

db_pt3()
df

print talib.get_functions()
print talib.get_function_groups()

t = talib.CDLDRAGONFLYDOJI(df['o'],df['h'],df['l'],df['c'])
t
ls = []

for i in t.iteritems():
    if i[1] == 100:
        ls.append(df['symbol'][i[0]])
ls

t2 = talib.CDLDRAGONFLYDOJI(df['o'],df['h'],df['l'],df['c'])
ls2 = []
for for i in t.iteritems():
    if i[1] == 100:
        ls.append(df['symbol'][i[0]])

def place_order():
    for i in ls:
        data_order = {
          "symbol":i,
          "qty":1,
          "type":2,
          "side":1,
          "productType":"CNC",
          "limitPrice":0,
          "stopPrice":0,
          "validity":"DAY",
          "disclosedQty":0,
          "offlineOrder":"True",
          "stopLoss":0,
          "takeProfit":0
        }
        fyers.place_order(data_order)
place_order()

