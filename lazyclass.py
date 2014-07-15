 
 
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
     
    def differenceXY(self,x=None,y=None):
        if (x==None and y!=None) or (x!=None and y==None):
            raise XanaError('NeedBothError')
        if x!=None and y!=None:
            if len(x)!=len(y):
                raise XanaError('NeedSameLength')
        if x==None:
            x=self.x
        if y==None:
            y=self.y
        
        diff = [self.x[i]-self.y[i] for i in range(len(self.x))]
        return diff
     
    def printDefaults(self,x=1,y=3,z=4):
        print 'x=',x
        print 'y=',y
        print 'z=',z

# increase the values by 1
# calculate the product
    def newFun(self):
        print self.x
        self.x = [self.x[i]+i for i in range(len(self.x))]
        print self.x
        
        print self.y
        self.y = [self.y[i]+i for i in range(len(self.y))]
        print self.y
        
        prod = [self.x[i]*self.y[i] for i in range(len(self.x))]
        return prod
        
        

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