import os
import csv
import lazyclass

dirName = '/Users/Miranda/git/Random Data'
fileName = 'sampleData.dat'

with open(os.path.join(dirName,fileName),'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ',')
    data = list()
    for row in dataReader:
        data.append(row)
data.pop(0)
print data
x = [int(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]
z = [float(data[i][2]) for i in range(len(data))]
# print x,y,'ran'

xyObj = lazyclass.simpleOperations(x,y)
# print xyObj.productXY()
print xyObj.differenceXY()

xzObj = lazyclass.simpleOperations(x,z)
yzObj = lazyclass.simpleOperations(y,z)

print xzObj.differenceXY()
print yzObj.differenceXY()