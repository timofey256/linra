from matrix import Matrix
import math

class Ortogonalization:
    """
        Default euclidian dot product.
        x and y should be lists of the same size.
    """
    @staticmethod
    def _default_dot_product(x, y):
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
        print("vectors: ", vectors)
        for i in range(len(vectors)):
            t = Matrix([0 for i in range(len(vectors[0]))])
            j=0
            while j<i:
                print(dot_product(vectors[i], z[j]))
                t += dot_product(vectors[i], z[j])*z[j]
                j += 1
            y_i = Matrix(vectors[i]) - t
            norm_y = math.sqrt(dot_product(y_i, y_i))
            z_i = y_i/norm_y
            print(f"i: {i}, t: {t} y: {y_i}, z_i: {z_i}")
            z.append(Matrix(z_i))
        return z
