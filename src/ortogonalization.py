import matrix

class Ortogonalization:
    """
        Default euclidian dot product.
        x and y should be lists of the same size.
    """
    @staticmethod
    def _default_dot_product(x, y):
        if (len(x) != len(y)):
            raise ValueError("Vectors should be of the same size.")
        
        n = len(x)

        product = 0
        for i in range(n):
            result += x[i]*y[i]

        return product

    """
        Gram-Schmidt ortogonalization of vectors. Non-standard dot product could be given as a parameter.
        'vectors' is a required parameter of list type.
    """
    @staticmethod
    def gram_schmidt(vectors, dot_product=_default_dot_product()):
        for i in range(len(vectors))
            y = vectors
            #TODO
