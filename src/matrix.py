class Matrix:
    def __init__(self, arr):
        rows = len(arr)
        col = len(arr[0]) if type(arr[0])==type(list) else 1
       
        if (rows <= 0 or col <= 0):
            raise ValueError("Dimensions of the matrix should be greater than 0.");

        self.rows = rows
        self.col = col
        self.matrix = arr

    def __eq__(self, other):
        return self.matrix == other.matrix

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
        if (type(other) != Matrix):
            raise TypeError(f"You can add only Matrix and Matrix. Given argument is {type(other)} type.")
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
    
    def __mul__(self, a):
        result = self.matrix.copy()
        # a is a scalar
        if type(a) == int or type(a) == float:
            for i in range(self.rows):
                for j in range(self.col):
                    if (self.col != 1):
                        result[i][j] *= a
                    else: 
                        result[i] *= a
        # dot product: only for vectors
        else:
        #TODO
            pass
        return Matrix(result)

    def __truediv__(self, a):
        result = self.matrix.copy()
        if type(a) == int or type(a) == float:
            for i in range(self.rows):
                for j in range(self.col):
                    if self.col != 1:
                        result[i][j] /= a
                    else:
                        result[i] /= a
        else:
            raise ValueError("You can't divide a matrix by anything but scalar.")
        return Matrix(result)

    def __repr__(self):
        return str(self.matrix)
