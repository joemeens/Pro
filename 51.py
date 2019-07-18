a1=int(input())
a2=list(map(int,input().split(" ")))
a3=sorted(a2)
print(a3[min(a3)-1])
