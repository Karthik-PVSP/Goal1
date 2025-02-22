def printDiamond(N):
    # Code here
    totalrows=N*2
    nstars=1
    for row in range(0,totalrows):
        if(row>totalrows/2):
            nstars-=1
        #for spaces
        for space in range(0,N-nstars):
            print(" ",end="")
        for element in range(0,nstars):
            print("* ",end="")
        if(row<=totalrows/2):
            if(nstars==N):
                nstars=nstars
            else:
                nstars+=1
        
        print("")
printDiamond(int(input()))