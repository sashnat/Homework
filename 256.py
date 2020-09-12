import datetime
today = datetime.datetime.now()
print(today, datetime.datetime(today.year, 1, 1))
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
if day_of_year == 256:
    print("С днем программиста!!!")
