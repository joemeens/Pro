str1=input()
for pok in str1:
    if(pok.islower()):
        print(pok.upper(),end="")
    else:
        print(pok.lower(),end="")
