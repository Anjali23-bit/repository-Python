string =input()
substring =input()
res = sum(1 for i in range(len(string)) 
        if string.startswith(substring, i))
print(res)        
 