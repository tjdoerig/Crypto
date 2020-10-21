import pandas as pd

def StartEndtime(starttime = 1577836800000, endtime = 1577923200000, deltatime = 86400000):


    if endtime > starttime:
        
        nNumRequests = int((endtime-starttime) / deltatime)
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

    return 


dfTime = StartEndtime(endtime=1578009600000)
print(dfTime)