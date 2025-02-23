n=int(input("Enter number to find it's factorial"))
def findFact(n:int)->int:
    if n==0 or n==1:
        return 1
    else:
        return n*findFact(n-1)
print(findFact(n))