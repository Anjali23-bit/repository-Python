def OperationChoices(c,a,b):
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)    
    elif c==3:
        print(a*b)    
    elif c==4: 
        print(a/b)
    else:
        print(" ")
c=int(input("c: "))  
a=int(input("a: "))    
b=int(input("b: "))  
print(OperationChoices(c,a,b)) 