def ispalindrome(s):
    return s==s[: : -1]
s=input(" ")
p=ispalindrome(s)
if p:
    print("Yes")
else:
    print("No")
