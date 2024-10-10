n=int(input())
list1=[int(num) for num in input().split(" ",n-1)]
dup=[]
for a in list1:
    if list1.count(a) > 1:
        if a not in dup:
            dup.append(a)
print(len(dup))