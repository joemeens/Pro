num=input()
a1=list(map(int,input().split(" ")))
b1=list(map(int,input().split(" ")))
if(len(a1)==len(b1)):
    for i in a1:
        for j in b1:
            if(i==j):
                print(i,end=" ")
            else:
                continue
