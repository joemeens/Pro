a=input()
l=["a","e","i","o","u","A","E","I","O","U"]
for i in a:
    if i  in l:
        a=a.replace(i,"")
     
       
print(a[::-1])
    
