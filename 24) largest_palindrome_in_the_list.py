def palindrome(list1):
    c = 0
    for i in list1:
        if str(i) ==str(i)[::-1]:
            print(i)
            c += 1
            list2=[]
            list2.append(i)
    print("Total palindrome nos. are", c)
    print(max(list2))
list1= [1,232,54545,999991]
palindrome(list1)
