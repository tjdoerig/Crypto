import requests
import json
import time
import numpy as np
import pandas as pd

#Documentation:
#"https://docs.bitfinex.com/reference#rest-public-platform-status"

#UTC time -> 01.01.2020 00:00:00 Uhr -> in ms 1577836800000
#https://api-pub.bitfinex.com/v2/candles/trade:1m:tBTCUSD/hist?limit=100&start=1577836800000&end=1577837400000&sort=-1
#86400000 (MTS von einem Tag)

#########Define to Start##########
STARTTIME = 1577836800000
ENDTIME = 1578096000000
#########End Define to Start##########

#static 
PROTOCOL = "https"
HOST = "api-pub.bitfinex.com" #"api.bitfinex.com"
VERSION = "v2"
ENDPOINTS = "candles"
TIMEFRAME = "trade:1m"
SYMBOL = "tBTCUSD"
SECTION = "hist"
LIMIT = "3600" #seconds per one day -> max. requested: 10000
SORT = "1"
nState = 0

def APICALL(protocol, host, version, endpoints, timeframe, symbol, selection, limit, starttime, endtime, sort):
    URL = "{0:s}://{1:s}/{2:s}/{3:s}/{4:s}:{5:s}/{6:s}?limit={7:s}&start={8:s}&end={9:s}&sort={10:s}".format(protocol, host, version, endpoints, timeframe, symbol, selection,limit, starttime, endtime, sort)
    response = requests.get(URL)

    if response.ok:
            li = response.json()#pd.DataFrame(response.json())
            #print(df)
            #df.columns = ['MTS', 'OPEN', 'CLOSE', 'HIGH', 'LOW', 'VOLUME']
            return li
    else:
        raise ValueError(response)

def StartEndtime(starttime = 1577836800000, endtime = 1577923200000, deltatime = 86400000):
    if endtime > starttime:

        #calc iteration of how many day's
        nNumRequests = int((endtime-starttime) / deltatime)

        #empty DataFrame
        dfTime = pd.DataFrame()

        #add new times to the df
        for i in range(nNumRequests):
            liTime = [[str(starttime),str(endtime)]]
            dfTime = dfTime.append(liTime, ignore_index=True)         
            starttime = endtime
            endtime += deltatime

            #label the columns
            if i+1 == nNumRequests:
                dfTime.columns = ['Starttime', 'Endtime']                
        
        return dfTime

    else:
        raise ValueError("Start-/Endtime incorrect")

#Mainloop
while True:    
    if nState == 0:
        #Get TimeDataframe for each day
        dfTime = StartEndtime(starttime=STARTTIME, endtime=ENDTIME)
        
        data = pd.DataFrame()
        
        for index, row in dfTime.iterrows():
            Starttime = row[0]
            ENDTIME = row[1]
            li1 = APICALL(PROTOCOL,HOST,VERSION,ENDPOINTS,TIMEFRAME,SYMBOL,SECTION,LIMIT,Starttime,ENDTIME,SORT)  
            time.sleep(1)
            data = data.append(li1)

        #End of this state
        nState += 1
      

    #Stopp Sate
    elif nState == 1: 
        #df.to_csv('GfG.csv', index = True)
        print(data)
        break 

    else:
        raise ValueError("State fault")
