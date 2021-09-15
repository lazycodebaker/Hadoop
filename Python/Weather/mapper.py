

import sys

data = open("weather.txt",'r')



for line in data.readlines():
    row = str(line.strip())
    date = row[6:14]
    max_temp = float(row[39:45])
    min_temp = float(row[47:53])

    if max_temp > 30.0:
        print("HOT-DAY:",date,max_temp)

    if min_temp < 15:
        print("COLD-DAY:",date,min_temp)
        

