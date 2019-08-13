num1,num2=map(int,input().split(" "))
get_the_list=list(map(str,input().split(" ")))
new=str(" ".join(get_the_list[:-num2]))
print(new)
