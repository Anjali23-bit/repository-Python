def operator(str1):
    for i in range(0,len(str1)):
        if (str1[i]=='(' or str1[i]==')'):
           continue
        print(str1[i], end='')
    return " "
str1='(x+y)+(z+q)'
print(operator (str1))
