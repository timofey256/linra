class Matrix:
    def __init__(self, arr):
        self.rows = len(arr)
        self.col = len(arr[0]) if type(arr[0])==list else 1
        self._data = arr if type(arr[0]) == list else [arr] # if vector is given
        
        if (self.rows <= 0 or self.col <= 0):
            raise ValueError("Dimensions of the matrix should be greater than 0.");

    @staticmethod
    def create_zero_matrix(rows_number, cols_number):
        arr = []
        for i in range(rows_number):
            arr.append(cols_number*[0])
        return Matrix(arr)
    
    @staticmethod
    def create_unit_matrix(rows_number, cols_number):
        m = Matrix.create_zero_matrix(rows_number, cols_number)
        for i in range(rows_number):
            m._data[i][i] = 1
        return m

    def __eq__(self, other):
        return self._data == other._data

    def __sub__(self, other):
        self._validate_matrix(other)
        
        res = []
        for k in range(self.rows):
            res.append([0 for i in range(self.col)])
        for i in range(self.col):
            for j in range(self.rows):
                res[i][j] = self._data[i][j] - other._data[i][j]

        return Matrix(res)

    def __add__(self, other):
        self._validate_matrix(other)
        res = []
        for k in range(self.rows):
            res.append([0 for i in range(self.col)])
        
        for i in range(self.rows):
            for j in range(self.col):
                res[i][j] = self._data[i][j] + other._data[i][j]

        return Matrix(res)
    
    def __mul__(self, other):
        result = None
        # a is a scalar
        if type(other) == int or type(other) == float:
            result = self._data.copy()
            for i in range(self.rows):
                for j in range(self.col):
                    if (self.col != 1):
                        result[i][j] *= other
                    else: 
                        result[i] *= other
        # a is an another matrix
        elif type(other)==Matrix:
            self._validate_matrix(other)

            result = Matrix.create_zero_matrix(self.rows, self.col)._data
            for i in range(self.rows):
                for j in range(other.col):
                    element = 0
                    for k in range(self.col):
                        element += self._data[i][k]*other._data[k][j]
                    result[i][j] = element
        return Matrix(result)

    def __truediv__(self, a):
        result = self._data.copy()
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
        return str(self._data)

    def transpose(self):
        matrix = self._data.copy()
        for i in range(self.rows):
            for j in range(i, self.col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        return Matrix(matrix)

    def _validate_matrix(self, matrix):
        if (type(matrix) != Matrix):
            raise TypeError(f"You can add only Matrix and Matrix. Given argument is {type(matrix)} type.")
        if (self.rows != matrix.rows or self.col != matrix.col):
            raise ValueError("Matrices should be of the same size to perform addition.")        