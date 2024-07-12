n1=int(input("Enter the no of students placed in CSE:"))
n2=int(input("Enter the no of students placed in ECE:"))
n3=int(input("Enter the no of students placed in MECH:"))
if n1>n2:
    if n1>n3:
        print("Highest placement")
        print("CSE")
elif n2>n1 and n2>n3:
    print("Highest placement")
    print("ECE")
elif n3>n1 and n3>n2:
    print("Highest placement") 
    print("MECH")  
elif n1<0 or n2<0 or n3<0:
    print("Input is invalid")
elif n1==n2==n3:
    print("None of the department has got the highest placement")    
else:
    print(" ")  
