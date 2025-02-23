#Problem-4 Generate all the strings of length N drawn from 0...k-1 
#means we need to genreate strings of length n using values from 0 to k-1
from typing import List

def toList(k: int) -> List[str]:
    result = []
    for x in range(0, k):
        result.append(str(x))
    return result

def baseKStrings(n, k):
    if n == 0: return []
    if n == 1: return toList(k)
    return [str(digit) + bitstring for digit in baseKStrings(1, k) for bitstring in baseKStrings(n-1, k)]

print(baseKStrings(2, 2))
