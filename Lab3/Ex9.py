def Findplace(matrix):
    blocked = []
    
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i):
                if matrix[k][j] >= matrix[i][j]:
                    blocked.append((i, j))
                    break
    
    return blocked

matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

blockedspectators = Findplace(matrix)
print(blockedspectators)
