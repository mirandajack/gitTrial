import os
import csv
import random as rand
import matplotlib.pyplot as plt

x = range(1,10)
y = [(i+rand.random())**2 for i in x]
z = [(i+rand.random()*2)**2 for i in x]

print x
print y

plt.figure()
font = {'family': 'Times New Roman', 'size':16}
plt.rc('font', **font)
plt.plot(x,y,'o')
plt.title('with noise')
plt.xlabel('x (sec)')
plt.ylabel('x**2+e (volt)')
plt.show()

dirName = '/Users/Miranda/git/Random Data'
fileName = 'sampleData.dat'

dataList = list()
[dataList.append([x[i],y[i],z[i]]) for i in range(len(x))]

print dataList
  
with open(os.path.join(dirName,fileName),'w') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['x','y','z'])
    writer.writerows(dataList)