
import sys

temp_dict = {}

for line in sys.stdin:
    key , date , value  = line.strip().split(' ')

print(key,date,value)

