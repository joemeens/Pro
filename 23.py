a,b=map(int,input().split(" "))
a1=list(map(int,input().split(" ")))
a2=list(map(int,input().split(" ")))
for i in a2:
    a1.insert(0,i)
    c3=max(a1)
    print(c3,end=" ")
 
