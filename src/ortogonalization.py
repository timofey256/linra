from matrix import Matrix
import math

class Ortogonalization:
    """
        Default euclidian dot product.
        x and y should be lists of the same size.
    """
    @staticmethod
    def _default_dot_product(x, y):
        print(x, y)
        x = x if type(x)==list else x.matrix
        y = y if type(y)==list else y.matrix
        if (len(x) != len(y)):
            raise ValueError("Vectors should be of the same size.")
        
        n = len(x)

        product = 0
        for i in range(n):
            product += x[i]*y[i]

        return product

    """
        Gram-Schmidt ortogonalization of vectors. Non-standard dot product could be given as a parameter.
        'vectors' is a required parameter of list type.
    """
    @staticmethod
    def gram_schmidt(vectors, dot_product=_default_dot_product):
        z = []
        for i in range(len(vectors)):
            t = Matrix([0 for i in range(len(vectors[0]))])
            for j in range(i):
                t += dot_product(vectors[i], z[j])*z[j]
            y = Matrix(vectors[i]) - t
            norm_y = math.sqrt(dot_product(y, y))
            z_i = y/norm_y
            z.append(z_i)
        return z
