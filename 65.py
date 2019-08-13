numb=int(input())
list1=map(int,input().split(" "))
for numbers in list1:
    if(numbers<numb):
        print(numbers,end=" ")
