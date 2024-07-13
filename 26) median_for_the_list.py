def median(list1):
    list1.sort()
    print(list1)
    n=len(list1)
    m=n//2
    if n %2 ==0:
        m1=m-1
        m2=m
        m=(m1+m2)/2
        return list[m]
    else:
        m=list1[m]
        return m
list1=[4,12,56,23,7,6,9]        
print(median(list1))
