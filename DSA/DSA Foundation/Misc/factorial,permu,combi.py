n=int(input())
r=int(input())
def fact(n:int)->int:
    sumcounter=1
    for x in range(1,n+1):
        sumcounter*=x
    return sumcounter
nfact=fact(n)
nrfact=fact(n-r)
rfact=fact(r)
permu=nfact/(nrfact)
print(nfact)
print(int(permu))
print(int(permu/rfact))