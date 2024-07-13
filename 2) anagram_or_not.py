a=str(input(" "))
b=str(input(" "))
x=a.lower()
y=b.lower()
if(len(a)==len(b)):
    s1=sorted(x)
    s2=sorted(y)
    if(s1==s2):
        print(a,b,"are anagram")
    else:
        print(a,b,"are not anagram")
