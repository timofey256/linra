#!/bin/usr/env python3

import numpy as np


class Diagonalization:
    """
        Gets matrix of quadratic form and returns its diagonalization: 
        diagonal matrix D and transition matrix Q. Then A = Q^{T} A Q

        A should be a symetric matrix.
    """
    @staticmethod
    def diagonalize_form(A):
        n, m = np.array(A).shape
        if n != m:
            raise ValueError("A should be a square matrix")

        I = np.identity(n).tolist()
        
        for k in range(n):
            potential_pivots  = [abs(A[i][k]) for i in range(n)]

            A = np.transpose(np.array(A)).tolist()
            
            for i in range(k+1, n):
                c = A[i][k] / A[k][k]
                for j in range(k+1, n):
                    A[i][j] = round(A[i][j] - c * A[k][j],2)    
                A[i][k] = 0

                for j in range(k+1, n):
                    A[j][i] = round(A[j][i] - c * A[j][k], 2)
                A[k][i] = 0 
                
                for j in range(k, n):
                    I[j][i] = round(I[j][i] - c * I[j][k], 2)
                
        return (A, I)
