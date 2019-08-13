amber,counting=map(int,input().split(" "))
array=list(map(int,input().split(" ")))
count=0
for i in range(0,len(array)):
    count=1
    for j in range(i+1,len(array)):
        if(array[i]==array[j]):
            count=count+1
    if(count==counting):
        print(array[i])
