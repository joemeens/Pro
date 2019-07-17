str1=input()
f=[]
a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in str1:
    if(i=="X"):
        f.append("A")
    elif(i=="Y"):
        f.append("B")
    else:
        f.append(a1[a1.index(i)+3])
print("".join(f))
