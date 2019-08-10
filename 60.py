list1,str2=map(str,input().split(" "))
count=0
for i in range(0,len(list1)):
        for j in range(0,len(str2)):
            if(list1[i]==str2[j]):
                count=count+1
            else:
                continue
if(count>=1):
    print("yes")
else:
    print("no")
