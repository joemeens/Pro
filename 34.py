name=input()
if(len(name)>=3):
    for i in range(0,len(name)):
        if(i%3==0):
            print(name[i],end="")
