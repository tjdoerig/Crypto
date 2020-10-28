import requests
import json
import time
import numpy as np
import pandas as pd
'''
#Documentation:
#"https://docs.bitfinex.com/reference#rest-public-platform-status"

#UTC time -> 01.01.2020 00:00:00 Uhr -> in ms 1577836800000
#https://api-pub.bitfinex.com/v2/candles/trade:1m:tBTCUSD/hist?limit=100&start=1577836800000&end=1577837400000&sort=-1
#86400000 (MTS von einem Tag)

#########Define to Start##########
STARTTIME = 1577836800000
ENDTIME = 1578096000000
#########End Define to Start##########

def StartEndtime(starttime = 1577836800000, endtime = 1577923200000, deltatime = 86400000):
    if endtime > starttime:
        #calc iteration of how many day's
        nNumRequests = int((endtime-starttime)/deltatime)

        #empty DataFrame
        dfTime = pd.DataFrame()
        
        #add new times to the df
        for i in range(nNumRequests):
            #coloumn names
            liTime = [[str(starttime),str(starttime+deltatime)]]
            dfTime = dfTime.append(liTime, ignore_index=True)         
            
            starttime = starttime+deltatime

            #label the columns
            if i+1 == nNumRequests:
                dfTime.columns = ['Starttime', 'Endtime']                

        return dfTime

    else:
        raise ValueError("Start-/Endtime incorrect")



dfTime = StartEndtime(STARTTIME,ENDTIME)

print(dfTime)
'''
print(pd.to_datetime(1603790815946, unit='ms'))