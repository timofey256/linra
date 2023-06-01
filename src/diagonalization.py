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
                c = A._data[i][k] / A._data[k][k]
                
                # Substitute rows of A
                for j in range(k+1, n):
                    A._data[i][j] = Diagonalization._round_number(A._data[i][j] - c * A._data[k][j])
                A._data[i][k] = 0

                # Substitute columns of A
                for j in range(k+1, n):
                    A._data[j][i] = Diagonalization._round_number(A._data[j][i] - c * A._data[j][k])
                A._data[k][i] = 0 

                # Substitute columns of I
                for j in range(n):   
                    I._data[j][i] = Diagonalization._round_number(I._data[j][i] - c * I._data[j][k])
                
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