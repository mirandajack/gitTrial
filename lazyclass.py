 
 
class simpleOperations(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
         
# all of simple operations can call x because of this self function
 
    def productXY(self):
        prod = [self.x[i]*self.y[i] for i in range(len(self.x))]
        return prod
         
    def addOneX(self):
        print self.x
        self.x = [self.x[i]+i for i in range(len(self.x))]
        print self.x
        return None
     
    def differenceXY(self):
        diff = [self.x[i]-self.y[i] for i in range(len(self.x))]
        return diff
     
     
#         
# x = [2,5,3]
# y = [4,5,7]
# 
# ranObj = simpleOperations(x,y)
# prod = ranObj.productXY()
# 
# print x, y, prod
# 
# ranObj = simpleOperations(x,y)
# 
# ranObj.addOneX()
# 
# ranObj.addOneX()