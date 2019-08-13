number,num=map(str,input().split(" "))
a1=list(map(str,input().split(" ")))
l=[]
for i in a1:
    if(int(i)<int(num)):
        l.append(i)
a2=sorted(l)
print(' '.join(a2))
