class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print("\t", self.matrix[i][j], end="")
            print()

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print("\t", self.matrix[i][j] + other.matrix[i][j], end="")
            print()


m_1 = Matrix([[1, 7], [7, 9], [4, 8]])
m_2 = Matrix([[3, 2], [5, 4], [7, 3]])

print(m_1 + m_2)

