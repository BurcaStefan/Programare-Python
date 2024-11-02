def Replacediagonali(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j<i:
                matrix[i][j]=0
    return matrix

matrix=[[1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]] 

result=Replacediagonali(matrix)

for i in range(len(result)):
    print(result[i])