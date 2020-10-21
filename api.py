import requests
import json
import time
import numpy as np
import pandas as pd

#Documentation:
#"https://docs.bitfinex.com/reference#rest-public-platform-status"

#UTC time -> 01.01.2020 00:00:00 Uhr -> in ms 1577836800000

PROTOCOL = "https"
HOST = "api-pub.bitfinex.com" #"api.bitfinex.com"
VERSION = "v2"
ENDPOINTS = "candles"
TIMEFRAME = "trade:1m"
SYMBOL = "tBTCUSD"
SECTION = "hist"
LIMIT = "2"
SORT = "-1"

def APICALL(protocol, host, version, endpoints, timeframe, symbol, selection, limit,sort):
    #return
    #Fields	Type	Description
    #MTS	int	    millisecond time stamp
    #OPEN	float	First execution during the time frame
    #CLOSE	float	Last execution during the time frame
    #HIGH	float	Highest execution during the time frame
    #LOW	float	Lowest execution during the timeframe
    #VOLUME	float	Quantity of symbol traded within the timeframe

    #URL = "https://api-pub.bitfinex.com/v2/candles/trade:1h:tBTCUSD/hist?limit=2&sort=-1" 
    #'https://api-pub.bitfinex.com/v2/candles/trade:1m:tBTCUSD/last?limit=10&sort=-1'#
    URL = "{0:s}://{1:s}/{2:s}/{3:s}/{4:s}:{5:s}/{6:s}?limit={7:s}&sort={8:s}".format(protocol, host, version, endpoints, timeframe, symbol, selection,limit,sort)
    response = requests.get(URL)

    if response.ok:
        if selection == "hist":
            df = pd.DataFrame(response.json())
            df.columns = ['MTS', 'OPEN', 'CLOSE', 'HIGH', 'LOW', 'VOLUME']
            return df
        elif selection == "last":
            responseData = response.json()

            #Parse Data
            responseData = pd.DataFrame(responseData).T   

            #Change columns names 
            responseData.columns = ['Date', 'Open', 'Close', 'High', 'Low', 'Volume']

            
            #Parse "Date" -> not done!
            responseData = responseData.set_index(pd.DatetimeIndex(responseData["Date"].values))
            responseData.index.name = "Date"
           

            return print(responseData)
    else:
        raise ValueError(response)


data = APICALL(PROTOCOL,HOST,VERSION,ENDPOINTS,TIMEFRAME,SYMBOL,SECTION,LIMIT,SORT)
print(data)
