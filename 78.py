a,b=map(int,input().split(" "))
get_1=list(map(str,input().split(" ")))
get_2=list(map(str,input().split(" ")))
if(len(get_1)==a and len(get_2)==b):
    get_3=get_1+get_2
    get_4=sorted(get_3)
print(' '.join(get_4))
