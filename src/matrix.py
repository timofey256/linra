class Matrix:
    def __init__(self, arr):
        self.rows = len(arr)
        self.col = len(arr[0]) if type(arr[0])==list else 1
        self.matrix = arr
        
        if (self.rows <= 0 or self.col <= 0):
            raise ValueError("Dimensions of the matrix should be greater than 0.");
        
    @staticmethod
    def create_zero_matrix(rows_number, cols_number):
        arr = []
        for i in range(rows_number):
            arr.append(cols_number*[0])
        return Matrix(arr)

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __sub__(self, other):
        self._validate_matrix(other)
        
        res = []
        for k in range(self.rows):
            res.append([0 for i in range(self.col)])
        
        for i in range(self.rows):
            for j in range(self.col):
                res[i][j] = self.matrix[i][j] - other.matrix[i][j]

        return Matrix(res)

    def __add__(self, other):
        self._validate_matrix(other)
        res = []
        for k in range(self.rows):
            res.append([0 for i in range(self.col)])
        
        for i in range(self.rows):
            for j in range(self.col):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(res)
    
    def __mul__(self, other):
        result = None
        # a is a scalar
        if type(other) == int or type(other) == float:
            result = self.matrix.copy()
            for i in range(self.rows):
                for j in range(self.col):
                    if (self.col != 1):
                        result[i][j] *= other
                    else: 
                        result[i] *= other
        # a is an another matrix
        elif type(other)==Matrix:
            self._validate_matrix(other)

            result = Matrix.create_zero_matrix(self.rows, self.col).matrix
            for i in range(self.rows):
                for j in range(other.col):
                    element = 0
                    for k in range(self.col):
                        element += self.matrix[i][k]*other.matrix[k][j]
                    result[i][j] = element
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

    def transpose(self):
        matrix = self.matrix.copy()
        for i in range(self.rows):
            for j in range(i, self.col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return Matrix(matrix)

    def _validate_matrix(self, matrix):
        if (type(matrix) != Matrix):
            raise TypeError(f"You can add only Matrix and Matrix. Given argument is {type(matrix)} type.")
        if (self.rows != matrix.rows or self.col != matrix.col):
            raise ValueError("Matrices should be of the same size to perform addition.")        