list1,char=map(str,input().split(" "))
count=0
for i in range(0,len(list1)):
    if(list1[i]==char):
        count=count+1
    else:
        continue
print(count)
