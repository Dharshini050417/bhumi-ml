import datetime
from datetime import date, datetime as dt 


now = dt.now()
year = now.year
month = now.month
day = now.day

def getYearFirst():
    firstDateOfYear = date(year, 1, 1)
    return firstDateOfYear

def getMonthFirst():
    firstDateOfMonth = date(year, month, 1)
    return firstDateOfMonth

def getTodayDate():
    todayDate = date(year, month, day)
    return todayDate

def getLastDate():
    try:
        with open("lastDate.txt", 'r') as file:
            lastDate = file.read().strip()
            lastDate = dt.strptime(lastDate, "%Y-%m-%d").date() 
    except FileNotFoundError:
        lastDate = getYearFirst()  
    
    return lastDate
