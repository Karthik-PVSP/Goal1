starRows=int(input())
nspace=1
nstar=int((starRows-nspace+2)/2)

for x in range(1,starRows+1):

    for star in range(1,nstar+1):
        print("*",end="") 
    for space in range(1,nspace+1):
        print(" ",end="")
    for star in range(1,nstar+1):
        print("*",end="") 
    if x<starRows/2:
        nstar-=1
        nspace+=2
    else:
        nstar+=1
        nspace-=2
    print("")