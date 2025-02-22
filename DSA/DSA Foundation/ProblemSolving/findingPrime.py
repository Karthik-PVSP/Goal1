number1=int(input())
factorCounter=0

for x in range(0,number1+1):
    if number1%x==0:
        if factorCounter>=2:
            break
        if(x==(number1/x)):
            factorCounter+=1
        else:
            #print(f"{x},{number1/x} is a factor")
            factorCounter+=2



print("Yay" if factorCounter==2 else "Nay")