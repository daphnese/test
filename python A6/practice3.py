class product:
    def __init__ (self,c,n,q,u,pr):
        self.code=c
        self.name=n
        self.qty=q 
        self.unitprice=u 
        self.price=pr
    def getprice(self):
        return self.qty*self.unitprice
    def report(self):
        return str(self.code)+" "+self.name+" "+str(self.qty)+" "+str(self.unitprice)+" "+str(self.price())
code=int(input("Enter Code="))
name=input("Enter Name=")
qty=int(input("Enter Qty="))
unitprice=float(input("Enter Unitprice="))
price=float(input("Enter Total"))
p=product(code,name,qty,unitprice,price)
print(p.report())