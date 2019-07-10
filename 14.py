anum=input()
list1=["a","e","i","o","u","A","E","I","O","U"]
for i in anum:
    if i  in list1:
        anum=anum.replace(i,"")
print(anum[::-1])
    
