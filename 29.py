import math
a,b=input().split(" ")
a=int(a)
b=int(b)
count=0
for num in range(a,b+1):
    root=math.sqrt(num)
    if(int(root+0.5)**2==num):
        count=count+1
    else:
        continue
print(count)
