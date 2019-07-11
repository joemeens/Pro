##Smallest number divisible by the given range:
a,b=input().split()
a=int(a)
b=int(b)
c=0
for i in range(2,b+1):
    if(a%i==0 and b%i==0):
         c=i
print(c)
