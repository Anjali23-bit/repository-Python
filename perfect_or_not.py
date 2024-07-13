def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        print(n,"is perfect")
    else:
        print(n,"is not perfect")
    return " "
print(perfect(28))
