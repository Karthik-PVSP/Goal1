number1=int(input())

printvalue="false"
for x in range(1,int(number1**0.5)+1):
    if x*x==number1:
        printvalue="true"
        break

print(printvalue)