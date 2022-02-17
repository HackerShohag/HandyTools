import sys
import os

filename = sys.argv[1]
file = open(filename,'r')
updatedData = file.read()
print(updatedData, end="")
prevData = ""

while True:
    file = open(filename,'r')
    data = file.read()
    if data != prevData:
        print(data.replace(prevData,""), end="")
    prevData = data
