while True:
    num=input("enter a number or '00' to exit: ")
    if(num=='00'):
        print("END")
        break
    #x=num[0]
    #y=num[1:]
    if(num.isdigit()):
        num=int(num)
        if(num==0):
            print("Neither even nor odd")
        if(num>0):
            if(num%2==0):
                print("+ve even")
            else:
                print("+ve odd")
    elif(num[0]=='-' and num[1:].isdigit()==True):
        num=int(num)
        if(num<0):
            if(num%2==0):
                print("-ve even")
            else:
                print("-ve odd")