n=int(input(" "))
n1=0
n2=1
n3=n1+n2
for i in range(3,n+1):
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1+n2
