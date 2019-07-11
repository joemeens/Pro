#check whether the two strings differ by oly one character
a,b,c=map(str,input().split())
count=0
for i in range(len(a)):
    #for j in range(0,len(b)):
    if(a[i]!=b[i]):
        count=count+1
if(count==c):
    print("yes")
else:
    print("no")
