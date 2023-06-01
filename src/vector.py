from .matrix import Matrix

class Vector(Matrix):
    def __init__(self, arr):
        self._data = arr
        self.rows = len(arr)
        self.cols = 1
    
    def __add__(self, other):
        self._validate_type(other)
        self._validate_size(other)
        res = list(map(lambda x, y: x+y, self._data, other._data))
        return Vector(res)
    
    def __radd__(other, self):
        return self.__add__(self, other)

    def __sub__(self, other):
        self._validate_type(other)
        self._validate_size(other)
        res = list(map(lambda x, y: x-y, self._data, other._data))
        return Vector(res)
    
    def __rsub__(other, self):
        return self.__sub__(other, self)
    
    def _validate_type(self, other):
        if type(other) != Vector:
            raise TypeError(f"You can perform this operation only with a Vector. {other} is not of type Vector.")
        
    def _validate_size(self, other):
        if len(self._data) != len(other._data):
            raise ValueError(f"Given vectors are not of the same size.")