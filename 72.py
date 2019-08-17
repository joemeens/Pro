a=int(input())
ab=list(map(str,input().split(" ")))
n1=len(ab)
l=[]
for i in range(n1-1):
    if(ab[i]<=ab[i+1]):
        l.append(ab[i+1]) 
print(max(l))
