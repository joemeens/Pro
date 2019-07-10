a,b=input().split()
a=int(a)
b=int(b)
for i in range(1,10000):
    if(i%a==0 or i%b==0):
        print(i)
        break
