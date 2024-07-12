n=int(input(" "))
rev=0
while n>0:
  rem=n%10
  rev=rev*10rem
  n=n//10
print(rev)
