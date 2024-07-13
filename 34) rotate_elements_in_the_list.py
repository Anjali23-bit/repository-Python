def rotate(L,d,n):
	list=[]
	list=L[d:]+L[0:d]
	return list
l=[1,2,3,4,5,6,7]
d=3
N=len(l)
l=rotate(l,d,N)
for i in l:
	print(i,end=" " )
