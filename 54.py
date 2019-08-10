str1,str2=input().split(" ")
count=0
if(len(str1)==len(str2)):
    for i in range(0,len(str1)):
        for j in range(0,len(str2)):
            if(str1[i]==str2[j]):
                count=1
            else:
                continue
if(count==1):
    print("yes")
else:
    print("no")
                
            
