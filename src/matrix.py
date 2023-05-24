class Matrix:
    def __init__(self, arr):
        rows = len(arr)
        col = len(arr[0]) if type(arr[0])==type(list) else 1
        
        if (rows <= 0 or col <= 0):
            raise ValueError("Dimensions of the matrix should be greater than 0.");

        self.rows = rows
        self.col = col
        self.matrix = arr

    def __sub__(self, other):
        if (self.rows != other.rows or self.col != other.col):
            raise ValueError("Matrices should be of the same size to perform subtraction.")
    
        res = [0 for i in range(self.rows)] if (self.col == 1) else [self.rows*[0 for i in range(self.col)]]
        for i in range(self.rows):
            if (self.col != 1):
                for j in range(self.col):
                    res[i][j] = self.matrix[i][j] + other.matrix[i][j]
            else:
                res[i] = self.matrix[i] - other.matrix[i] 

        return Matrix(res)

    def __add__(self, other):
        if (self.rows != other.rows or self.col != other.col):
            raise ValueError("Matrices should be of the same size to perform subtraction.")
    
        res = [0 for i in range(self.rows)] if (self.col == 1) else [self.rows*[0 for i in range(self.col)]]
        for i in range(self.rows):
            if (self.col != 1):
                for j in range(self.col):
                    res[i][j] = self.matrix[i][j] + other.matrix[i][j]
            else:
                res[i] = self.matrix[i] + other.matrix[i] 

        return Matrix(res)

    def __repr__(self):
        return str(self.matrix)
