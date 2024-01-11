class payment:
    def __init__ (self,h,r):
        self.hour=h
        self.rate=r
    def getsalary(self):
        return self.hour*self.rate 
    def report(self):
        return str(self.hour)+" "+str(self.rate)+" "+str(self.getsalary())
h=int(input("Enter hour="))
r=int(input("Enter rate="))
p=payment(h,r)
print(p.report()) 
        