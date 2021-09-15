
import sys


for row in sys.stdin:
    col = row.strip().split(',')
    for value in col:
        print('%s,%s'%(value,1))
        

