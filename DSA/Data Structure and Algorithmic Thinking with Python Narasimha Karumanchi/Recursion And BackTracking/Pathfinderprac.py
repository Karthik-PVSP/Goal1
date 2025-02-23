



def findPath(matrix,sourcePoint:tuple,MatrixSize:int):
    x,y=sourcePoint
    if x+1==MatrixSize and y+1==MatrixSize:
        return [(x,y)]
    if x+1<MatrixSize and matrix[x+1][y]==1:
        a=findPath(matrix,(x+1,y),MatrixSize)
        if a!=None:
            return [(x,y)]+a
    if y+1<MatrixSize and matrix[x][y+1]==1:
        b=findPath(matrix,(x,y+1),MatrixSize)
        if b!=None:
            return [(x,y)]+b






Matrix = [[ 1 , 1 , 1, 1 , 0], [ 0 , 1 , 0, 1 , 0], [ 0 , 1 , 0, 1 , 0], [ 0 , 1 , 0, 0 , 0], [ 1 , 1 , 1, 1 , 1] ] 
print(findPath(Matrix,(1,1),5))