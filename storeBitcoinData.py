import requests
import json
import time
import numpy as np
import pandas as pd

from pymongo import MongoClient, errors

#Settings
PROTOCOL = "https"
HOST = "api-pub.bitfinex.com" #"api.bitfinex.com"
VERSION = "v2"
ENDPOINTS = "candles"
TIMEFRAME = "trade:1m"
SYMBOL = "tBTCUSD"
SECTION = "hist"
LIMIT = "2"
SORT = "-1"

class Api():
    def __init__(self):
        None

    def apicall(self, protocol = 'https', host = 'api-pub.bitfinex.com' , version = 'v2', endpoints = 'candles', timeframe = 'trade:1h', symbol = 'tBTCUSD', selection = 'hist', limit = '100', sort = '-1'):
        #Documentation:
        #https://docs.bitfinex.com/reference#rest-public-platform-status

        #return
        #Fields	Type	Description
        #MTS	int	    millisecond time stamp
        #OPEN	float	First execution during the time frame
        #CLOSE	float	Last execution during the time frame
        #HIGH	float	Highest execution during the time frame
        #LOW	float	Lowest execution during the timeframe
        #VOLUME	float	Quantity of symbol traded within the timeframe

        URL = "{0:s}://{1:s}/{2:s}/{3:s}/{4:s}:{5:s}/{6:s}?limit={7:s}&sort={8:s}".format(protocol, host, version, endpoints, timeframe, symbol, selection,limit,sort)
        response = requests.get(URL)
        data = response.json()

        try:
            lst = data[1]
             #convert the list into a dict
            dct = {'Date': lst[0], 'Open':lst[1], 'Close':lst[2], 'High':lst[3], 'Low':lst[4], 'Volume':lst[5]}
            return dct

        except:
            raise ValueError(response)

'''
class StorageBase:
    def __init__(self, dbName):
        #default port is 27017
        DOMAIN = 'localhost:'
        PORT = 27017

        self.name = dbName

        try:
            # try to instantiate a client instance
            client = MongoClient(
                host = [ str(DOMAIN) + str(PORT) ],
                serverSelectionTimeoutMS = 3000 # 3 second timeout
            )

            #Get db-Names in Storage path
            dblist = myclient.list_database_names()

            #If db Name not exits it will generate a db with the name
            if not self.name in dblist:
                db = myclient[self.name]
                col = db["Data"]

        except errors.ServerSelectionTimeoutError as err:
            # set the client instance to 'None' if exception
            client = None

            # catch pymongo.errors.ServerSelectionTimeoutError
            print ("pymongo ERROR:", err)

    def StoreData(self, dct,dbName):
        
'''   


#Main
#create instance
apicall = Api()

#call instance
lastbtc = apicall.apicall(PROTOCOL,HOST,VERSION,ENDPOINTS,TIMEFRAME,SYMBOL,SECTION,LIMIT,SORT)
#lasteth = apicall.apicall(PROTOCOL,HOST,VERSION,ENDPOINTS,TIMEFRAME,"tETHUSD",SECTION,LIMIT,SORT)

print(lastbtc)
#print(lasteth)