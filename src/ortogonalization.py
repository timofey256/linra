from .matrix import Matrix
from .vector import Vector
import math

class Ortogonalization:
    """
        Default euclidian dot product.
        x and y should be lists of the same size.
    """
    @staticmethod
    def _default_dot_product(x, y):
        x = x if type(x)==list else x._data
        y = y if type(y)==list else y._data
        if (len(x) != len(y)):
            raise ValueError("Vectors should be of the same size.")
        
        n = len(x)

        product = 0
        for i in range(n):
            product += x[i]*y[i]

        return product

    """
        Gram-Schmidt ortogonalization of vectors. Non-standard dot product could be given as a parameter.
        'vectors' is a required parameter of list of Vectors type.
    """
    @staticmethod
    def gram_schmidt(vectors, dot_product=_default_dot_product):
        z = []

        for i in range(len(vectors)):
            t = Vector([0 for i in range(len(vectors[0]))])
            j=0
            while j<i:
                t += Vector(z[j].copy())*dot_product(vectors[i], z[j])
                j += 1
            y_i = Vector(vectors[i]) - t
            norm_y = math.sqrt(dot_product(y_i, y_i))
            z_i = y_i/norm_y
            z.append(z_i._data)
        return z
