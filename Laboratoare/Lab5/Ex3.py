class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0] * m for _ in range(n)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            raise KeyError("Matricile nu pot fi inmultite, nu corespund dimensiunile")
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                result.set(i, j, sum(self.get(i, k) * other.get(k, j) for k in range(self.m)))
        return result

    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, func(self.get(i, j)))
                
    def print(self):
        for i in range(self.n):
            print(self.data[i])

matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)
print(matrix.get(1, 2))
print("\nMatricea initiala:")
matrix.print()

print("\nTranspusa:")
transposed = matrix.transpose()
transposed.print()

print("\nInmultirea matricilor:")
matrix2=matrix.multiply(transposed)
matrix2.print()

print("\nMatricea initiala inmultita cu 2:")
matrix.apply(lambda x: x * 2)
matrix.print()
