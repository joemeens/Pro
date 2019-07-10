tez=input()
for k in range(len(tez)):
    if (k%2==0):
        print(tez[k+1],end='')
    else:
        print(tez[k-1],end='')
