number1=int(input())
factorCounter=0
listoffactors=[]
for x in range(1,number1+1):
    if number1%x==0:
        if (x or number1/x) in listoffactors:
            break
        if(x==(number1/x)):
            factorCounter+=1
        else:
            print(f"{x},{number1/x} is a factor")
            factorCounter+=2
            listoffactors.append(number1/x)

        listoffactors.append(x)
print(listoffactors)