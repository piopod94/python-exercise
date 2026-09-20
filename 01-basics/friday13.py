import datetime

year = int(input()) 

counter = 0
for month in range(1, 13):
    if datetime.date(year, month, 13).weekday() == 4:
        counter += 1
    else:
        counter += 0

print(counter)
