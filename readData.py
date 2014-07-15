import os
import csv
import numpy as np
import matplotlib.pyplot as plt

#helper function - have to put definite arguments before option 
# has to go after essential arguments

def ourFit(x,y,deg,xi=None):
    if xi == None:
        xi = x
    fitCoeff = np.polyfit(x,y,deg)
    fitPoly = np.poly1d(fitCoeff)
    return fitPoly(xi)
    
dirName = '/Users/Miranda/git/Random Data'
fileName = 'sampleData.dat'

# reading the data in from our input files
with open(os.path.join(dirName,fileName),'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ',')
    data = list()
    for row in dataReader:
        data.append(row)
data.pop(0)

# casting them from str to int/float
x = [int(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]
z = [float(data[i][2]) for i in range(len(data))]

print x

# q = [y[i]*z[i] for i in range(len(y))]
# print q

# degrees of polynomial for fit
deg = 2

yFitValues = ourFit(x,y,deg)
xRandom = [4.5,6.5,8.5]
yFitRandom = ourFit(x,y,deg,xRandom)

zFitValues = ourFit(x,z,deg)

# yFitCoeff = np.polyfit(x, y, deg)
# 
# #create polynomial fit equation
# yFitPoly = np.poly1d(yFitCoeff)
# 
# yFitValues = yFitPoly(x)

# print yFitCoeff
# print yFitPoly
# print yFitValues

#evaluating function at a point
# print yFitPoly(1)

plt.figure()
plt.plot(x,y,'o')
plt.plot(x,yFitValues)
plt.plot(xRandom,yFitRandom,'x')
plt.plot(x,z,'o')
plt.xlim(0,10)
plt.show()