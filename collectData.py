from getJsonAPI import getJson
from getDates import getLastDate,getTodayDate
from datetime import timedelta

startDate=getLastDate()
lastDate=getTodayDate()
dataList=[]

def collectData():
    currDate=startDate
    while(currDate<lastDate):
        data=getJson([],["totalUsers"],[[str(currDate),str(currDate)]],[])["data"]
        if (len(data)==0):
            data=[str(currDate),0]
        else:
            data=[str(currDate),int(data[0]["value1"])]
            
        # data[0]["date"]=str(currDate)
        dataList.append(data)
        print(data)
        currDate+=timedelta(days=1)

    return(dataList)

