def appendAtFront(x, L): 
    a=[x + element for element in L] 
    return a
def bitStrings(n): 
    if n == 0: return [] 
    if n == 1: return ["0", "1"] 
    else: 
        return (appendAtFront("0", bitStrings(n-1)) + appendAtFront("1", bitStrings(n-1))) 
print (bitStrings(3))   