def printFunction(n:int):
    if n==0:
         print(0)
    else:
        print(n)
        printFunction(n-1)
printFunction(100)