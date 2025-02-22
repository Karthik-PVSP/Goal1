starRows=int(input())
initializedNumber=0
for x in range(1,starRows+1):
    for y in range(1,x+1):
        initializedNumber+=1
        print(str(initializedNumber)+" ",end="")
    print("")