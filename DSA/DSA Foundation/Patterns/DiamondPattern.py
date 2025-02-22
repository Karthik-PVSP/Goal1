starRows=int(input())
nstar=1
nspace=int((starRows-nstar)/2)

for x in range(1,starRows+1):


    for space in range(1,nspace+1):
        print(" ",end="")

    for star in range(1,nstar+1):
        print("*",end="")    
    if x<starRows/2:
        nstar+=2
        nspace-=1
    else:
        nstar-=2
        nspace+=1
    print("")