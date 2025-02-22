n=int(input())
list1=[0]
for x in range(1,n+2):
    if(len(list1)<2):
        list1.append(x)
    elif(len(list1)==2):
        list1.append(sum(list1))
        _=list1.pop(0)
print(list1.pop(0))
    