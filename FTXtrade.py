import ccxt
import pandas as pd
import numpy as np
import math
import json
import time
import datetime
import loginFTX
import connectgoogle

exchange = loginFTX.loginx()
sheet   =  connectgoogle.opensheet()

def ordercreate(amount_p,avg_price,last_price,start_amount):
    #exchange.create_order('XRP-PERP','market',status,amount)
    #if(last_price - avg_price > 0)
    return 0

def checkposition():
    return (pd.DataFrame(data=exchange.private_get_positions()))

def checkbalance():
    return (pd.DataFrame(data=exchange.fetch_balance()))

def checkprice():
    return (pd.DataFrame(data=exchange.fetch_tickers('XRP-PERP')))

def calamount(start_price,start_amount,avg_price,step):
    if((start_price - avg_price)<0):
        return (start_amount+(math.round_down(start_price - avg_price,3)) * (step))
    else:
        return (start_amount+(math.round_up(start_price - avg_price,3)) * (step))
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
position = checkposition() 
price_xrp   =   checkprice()
ask_xrp =   price_xrp.iloc[0]
bid_xrp = price_xrp.iloc[4]
avg_price = (bid_xrp[0] + ask_xrp[0])/2
start_price = 0.19600
start_amount = 1000
step = 30000
amount_p = round(position["result"][0]["cost"] * 100) / (avg_price)





#order = checkbalance()
#ordercreate(status,amount,price)