a=int(input())
ab=list(map(str,input().split(" ")))
n1=len(ab)
for i in range(n1-1):
    if(ab[i]<=ab[i+1]):
        print(ab[i+1],end=" ")
    else:
        print(ab[i],end=" ")
