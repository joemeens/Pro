n,k=map(int,input().split(" "))
a1=list(map(int,input().split()))
for i in a1:
    if(i==k):
        print("yes")
        break
else:
    print("no")
    
