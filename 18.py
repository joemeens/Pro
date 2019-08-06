num=int(input())
list1=[]
for i in range(0,num):
    adam=input()
    list1.append(adam)
count=0
amber=sorted("kabali")
for i in list1:
    if(len(amber)==len(i)):
        if(amber==sorted(i)):
            count=count+1
        else:
            continue
print(count)
