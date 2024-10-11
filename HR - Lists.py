if __name__ == '__main__':
    N = int(input())
    list1= []
    for i in range(N):
        s=list(input().split())
        if s[0]=='insert':
            list1.insert(int(s[1]),int(s[2]))
        if s[0]=='remove':
            list1.remove(int(s[1]))
        if s[0]=='append':
            list1.append(int(s[1]))
        if s[0]=='sort':
            list1.sort()
        if s[0]=='pop':
            list1.pop()
        if s[0]=='reverse':
            list1.reverse()     
        if s[0]=='print':
            print(list1)