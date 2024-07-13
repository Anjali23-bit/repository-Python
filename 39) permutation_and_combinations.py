def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(fact(5))    
def perm(n,r,m):
    #perm=(fact(n)//fact(n-r))%m
    #return perm
    comb=(fact(n)//(fact(n-r)*fact(r)))%m
    return comb
print(perm(5,4,3))
