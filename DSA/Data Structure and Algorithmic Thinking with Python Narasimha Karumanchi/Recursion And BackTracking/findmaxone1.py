from typing import List, Tuple


def findMaxBlock(A: List[List[int]], r: int, c: int, L: int, H: int, visited: List[List[bool]]) -> int:
    if r < 0 or r >= L or c < 0 or c >= H or A[r][c] == 0 or visited[r][c]:
        return 0
    
    visited[r][c] = True
    size = 1  # Current cell
    
    # Search in eight directions
    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    for dr, dc in directions:
        size += findMaxBlock(A, r + dr, c + dc, L, H, visited)
    
    return size

def getMaxOnes(A: List[List[int]]) -> Tuple[int, List[Tuple[int, int]]]:
    if not A:
        return 0, []
    
    L, H = len(A), len(A[0])
    visited = [[False for _ in range(H)] for _ in range(L)]
    maxsize = 0
    max_locations = []
    
    for i in range(L):
        for j in range(H):
            if A[i][j] == 1 and not visited[i][j]:
                size = findMaxBlock(A, i, j, L, H, visited)
                if size > maxsize:
                    maxsize = size
                    max_locations = [(i, j)]
                elif size == maxsize:
                    max_locations.append((i, j))
    
    return maxsize, max_locations

# Example usage
zarr = [
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1]
]

maxsize, max_locations = getMaxOnes(zarr)
print("Number of maximum 1s are:", maxsize)
print("Locations of maximum 1s are:", max_locations)