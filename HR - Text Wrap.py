import textwrap
def wrap(string,width):
    split=[(string[i:i+width])for i in range(0,len(string),width)]
    return split
if __name__ == '__main__':
    string=input()
    width=int(input())
    output=wrap(string,width)
    for i in output:
        print(i)