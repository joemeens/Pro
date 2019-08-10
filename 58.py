list1=map(str,input().split(" "))
str1=input()
count=0
for i in list1:
    if(i==str1):
        count=count+1
    else:
        continue
print(count)
