arr=[127, 220, 246, 277,1, 321, 454, 534, 565, 933] 
def isArraySorted(A):
    if len(A)==1:
        return True
    return A[0]<A[1] and isArraySorted(A[1:])
print(isArraySorted(arr))