def numtri(h):
    for i in range(1,h+1):
        print()
        for j in range(1,i+1):
            print(j,end='')

def startri(h):
    for i in range(1,h+1):
        print(' '*(h-i)+'*'*i)

numtri(4)
print()
startri(3)
