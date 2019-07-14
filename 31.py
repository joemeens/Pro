braces=input()
start=0
end=0
for i in braces:
    if(i=="("):
        start=start+1
    elif(i==")"):
        end=end+1
if(start==end):
    print("yes")
else:
    print("no")
