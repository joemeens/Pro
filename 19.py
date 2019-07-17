number=int(input())
l=[]
for i in range(2,number+1):
    if(number%i==0):
        l.append(i)
    else:
        continue
    number=number//i
a=sorted(l)
print(*a)
