def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
            
    return str1[:gcd(len(str1), len(str2))]
str1=input()
str2=input()        
print(gcdOfStrings(str1,str2))