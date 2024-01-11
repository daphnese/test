class product:
    def __init__ (self,c,n,q,u):
        self.code=c
        self.name=n
        self.qty=q 
        self.unitprice=u 
    def getprice(self):
        return self.qty*self.unitprice
    def report(self):
        return str(self.code)+" "+self.name+" "+str(self.qty)+" "+str(self.unitprice)+" "+str(self.getprice())
p=product(1,"cola",100,0.5)
print(p.report())
p.code=2
p.qty=200
print(p.report())
 