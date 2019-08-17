a12,b12=map(int,(input().split(" ")))
l=[]
for i in range(a12,b12+1):
    if(i%2!=0):
        l.append(i)
    else:
        continue
print(sum(l))
