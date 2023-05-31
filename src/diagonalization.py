#!/bin/usr/env python3

from src.matrix import Matrix

class Diagonalization:
    _places_after_dot = 2

    """
        Gets matrix of quadratic form and returns its diagonalization: 
        diagonal matrix D and transition matrix Q. Then A = Q^{T} A Q

        A should be a symetric matrix.
    """
    @staticmethod
    def diagonalize_form(A):
        n, m = A.rows, A.col
        if n != m:
            raise ValueError("A should be a square matrix.")
        # elif (not A.is_symetric):
        #     raise ValueError("A should be a symetric matrix.")

        I = Matrix.create_unit_matrix(n,n)
        
        for k in range(n):
            A = A.transpose()

            for i in range(k+1, n):
                c = A.matrix[i][k] / A.matrix[k][k]
                
                # Substitute rows of A
                for j in range(k+1, n):
                    A.matrix[i][j] = Diagonalization._round_number(A.matrix[i][j] - c * A.matrix[k][j])
                A.matrix[i][k] = 0

                # Substitute columns of A
                for j in range(k+1, n):
                    A.matrix[j][i] = Diagonalization._round_number(A.matrix[j][i] - c * A.matrix[j][k])
                A.matrix[k][i] = 0 

                # Substitute columns of I
                for j in range(n):   
                    I.matrix[j][i] = Diagonalization._round_number(I.matrix[j][i] - c * I.matrix[j][k])
                
        return (A, I)

    @staticmethod
    def _round_number(n):
        element = round(n, Diagonalization._places_after_dot)
        return int(element) if Diagonalization._int_check(element) else element

    @staticmethod
    def _int_check(n):
        if (str(n)[len(str(n))-2:] == ".0"):
            return True
        
        return False