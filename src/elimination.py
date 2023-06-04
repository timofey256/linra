from .matrix import Matrix

class Elimination:
    """
    Gets an instance of Matrix type
    
    Returns the given matrix in REF (Matrix type).
    """
    @staticmethod
    def REF(A):
        Elimination._validate_type(A)
        matrix = A.get_matrix().copy()
        (n, m) = A.get_size()
        
        row = 0
        col = 0
        min_it = min(n,m)

        max_pivot_row_i = 0
        while row<min_it and col<min_it:
            if matrix[row][col] == 0:
                col += 1
                continue
            
            max_pivot_row_i = Elimination._find_greatest_pivot_row(matrix, row, col)

            Elimination._swap_rows(matrix, row, max_pivot_row_i)
            print("afted swap: ", matrix)

            pivot = matrix[row][col]
            for rr in range(row + 1, n):
                coef = matrix[rr][col] / pivot
                for cc in range(col, m):
                    matrix[rr][cc] -= coef * matrix[row][cc]

                    # convert number to int, when possible
                    if Elimination._is_possible_to_int(matrix[rr][cc]):
                        matrix[rr][cc] = int(matrix[rr][cc])

            row += 1
        return Matrix(matrix) 

    """
        Returns an index of the row with the greatest pivot within the given column.
    """
    @staticmethod
    def _find_greatest_pivot_row(matrix, row_index, column_index):
        n = len(matrix)

        max_pivot_index = row_index
        for j in range(row_index, n):
            if abs(matrix[j][column_index]) >= abs(matrix[max_pivot_index][column_index]):
                max_pivot_index = j

        return max_pivot_index

    def _swap_rows(matrix, i, j):
        matrix[i], matrix[j] = matrix[j], matrix[i]

    """
    Gets an instance of Matrix type
    
    Returns the given matrix in RREF (Matrix type).
    """
    @staticmethod
    def RREF(A):
        ref_matrix = Elimination.REF(A)
        (n, m) = A.get_size()
        matrix = ref_matrix.get_matrix().copy()
        print(matrix)
        
        row = n-1
        col = m-1
        while row >= 0:
            while matrix[row][col] != 0 and col >= 0:
                col -= 1
            
            # zero row
            if matrix[row][col] == 0:
                col = m-1
                row -= 1
                continue

            for rr in range(1, row-1):
                coef = matrix[rr][col] / matrix[row][col]
                for cc in range(m):
                    matrix[rr][cc] -= coef * matrix[row][cc]
            row -= 1

        return Matrix(matrix)

    @staticmethod
    def _is_possible_to_int(num : float):
        return float(int(num))==num

    @staticmethod
    def _validate_type(matrix):
        if type(matrix) != Matrix:
            raise TypeError(f"Given parameter is not a Matrix type, as required, but {type(matrix)} type.")