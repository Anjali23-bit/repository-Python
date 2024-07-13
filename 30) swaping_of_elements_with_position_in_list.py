list1=[12,35,9,56,24]
def swaplist(list1,pos1,pos2):
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    return list1
print(list1)
pos1=1
pos2=3
print(swaplist(list1,pos1,pos2))
