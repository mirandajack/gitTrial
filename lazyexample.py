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
# print data
x = [int(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]
z = [float(data[i][2]) for i in range(len(data))]
# print x,y,'ran'

xyObj = lazyclass.simpleOperations(x,y)

# xyObj.printDefaults()
# xyObj.printDefaults(2,5,6)
# xyObj.printDefaults(2,2)
# xyObj.printDefaults(z=3)

print xyObj.newFun()

# # print xyObj.productXY()
# print xyObj.differenceXY()
# 
# xzObj = lazyclass.simpleOperations(x,z)
# yzObj = lazyclass.simpleOperations(y,z)
#  
# print xzObj.differenceXY()
# print yzObj.differenceXY()
# 
# r = [4,7,2]
# s = [7,3,5]
# 
# # doesn't matter what the name of the variables you call is
# 
# print xyObj.difference(r,s)