import os
import csv

dirName = '/Users/Miranda/git/Random Data'
fileName = 'sampleData.dat'

with open(os.path.join(dirName,fileName),'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ',')
    data = list()
    for row in dataReader:
        data.append(row)
data.pop(0)

x = [int(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]
z = [float(data[i][2]) for i in range(len(data))]

