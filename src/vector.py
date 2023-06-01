from .matrix import Matrix

class Vector(Matrix):
    def __init__(self, arr):
        self._data = arr
        self.rows = len(arr)
        self.cols = 1
    
    def __add__(self, other):
        res = list(map(lambda x, y: x+y, self._data, other._data))
        return Vector(res)
    
    def __radd__(other, self):
        return self.__add__(self, other)

    def __sub__(self, other):
        res = list(map(lambda x, y: x-y, self._data, other._data))
        return Vector(res)
    
    def __rsub__(other, self):
        return self.__sub__(other, self)