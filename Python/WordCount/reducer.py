
import sys

dicts = {}

for line in sys.stdin:
    word,count = line.strip().split(',')
    if word in dicts:
        dicts[word] = int(dicts[word] + 1)
    else:
        dicts[word] = 1

print(dicts)
