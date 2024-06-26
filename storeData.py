from collectData import collectData
import csv
import os
from getDates import getTodayDate

dataList=collectData()

if (os.path.exists("data.csv")):
    file_exists=True
else:
    file_exists=False

with open("data.csv",'a',newline='') as file:
    csv_writer=csv.writer(file)
    if (not file_exists):
        csv_writer.writerow(["Date","Users"])
    csv_writer.writerows(dataList)

print("the data is successfully added in csv")

#updating lastdate in lastdate.txt

with open("lastDate.txt",'w') as file:
    file.write(str(getTodayDate()))

