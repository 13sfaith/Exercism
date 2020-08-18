class Matrix:
    def __init__(self, matrix_string):
        self.matrixList = matrix_string.split("\n")

    def row(self, index):
        return [int(n) for n in self.matrixList[index-1].split(" ")]


    def column(self, index):
        col = []

        for k in self.matrixList:
            col.append(int(k.split(' ')[index-1]))

        return col
