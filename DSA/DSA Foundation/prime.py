number1=int(input())
returnvalue="Prime"
for y in range(2,int(number1**0.5)+1):  
    if number1%y==0:
        returnvalue="Not Prime"
print(returnvalue)