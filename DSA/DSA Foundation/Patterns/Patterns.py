#Single row counter
# loopCounter=int(input())
# for item in range(0,loopCounter):
#     # TODO: write code...
#     print("*",end="")
#For multi row patterns like matrics
#rows = int(input("Enter number of rows: "))
#cols = int(input("Enter number of columns: "))
#for row in range(rows):
#    for col in range(cols):
#        print("*", end=" ")  # Ensures asterisks are printed on the same line
#    print()  # Moves to the next line after each row is printed

#Triangle pattern
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# starCounter=1
# for x in range(0,rows):
#     for y in range(0,starCounter):
#         print("*",end="")
#     starCounter+=1
#     print("")
#print following pattern (Diamond)
#-*-
#***
#-*-
#n=3
#n=5
#--*--
#-***-
#*****
#-***-
#--*--
#even we need to enter it's incorrect input \
# from math import ceil
# matrixInput=int(input("Matrix input"))
# if matrixInput%2==0:
#     raise AttributeError("matrix input value should be odd number")
#     exit
# midbound=ceil(matrixInput/2)
# for x in range(0,matrixInput):
#     if(x+1<=midbound):
#         lowbound=midbound-x
#         midbound=midbound+x
#     else:
#         lowbound=matrixInput
        #for 3rd row 
            #low=mid-1
        # for y in range(0,matrixInput):
        
# nsp:int=(matrixInput)//2
# print(nsp)
# nst:int=1
# for x in range(0,matrixInput):
#     for space in range(0,nsp):
#         print(" ",end="")
#     for start in range(0,nst):
#         print("*",end="")
#     for emptyspace in range(0,nsp):
#         print(" ",end="")
#     if(x<(matrixInput//2)):
#         nsp-=1
#         nst+=2
#     else:
#         nsp+=1
#         nst-=2
#     print("")

# Pattern: Diamond with - and space 
matrixInput=int(input("Matrix input"))
if matrixInput%2==0:
    raise AttributeError("matrix input value should be odd number")
    exit()
ndash=1
nstart=1+((matrixInput)//2)

for rows in range(0,matrixInput):
    print(ndash)
    print(nstart)
    for stars in range(0,nstart):
        print("*",end="")
    for ndash in range(0,ndash):
        print(" ",end="")
    for stars in range(0,nstart):
        print("*",end="")
    if(rows<=(matrixInput/2)):
        nstart-=1
        ndash+=2
    else:
        nstart+=1
        ndash-=2
    print("")
