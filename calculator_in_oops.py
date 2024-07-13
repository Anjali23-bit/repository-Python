class Calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def division(self,x,y):
        if y!=0:
            return x//y
        else:
            return "cannot divide by zero"
calculator=Calculator()
res=calculator.add(5,7)
print(res)
res=calculator.subtract(20,10)
print(res)
res=calculator.multiply(20,10)
print(res)
res=calculator.division(20,10)
print(res)
