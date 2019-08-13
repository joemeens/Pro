a,b=map(int,input().split(" "))
a1=list(map(int,input().split()))
b1=sum(a1)
count=0
for i in range(0,len(a1)):
    if(b-a1[i] in a1):
        count=1
    else:
        continue
if(count==1):
    print("yes")
else:
    print("no")
