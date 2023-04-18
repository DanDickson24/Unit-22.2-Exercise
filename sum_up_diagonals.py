def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # get the length of the matrix
    n = len(matrix)

    # initialize variables to hold the sum of the diagonals
    diagonal1_sum = 0
    diagonal2_sum = 0

    # loop through the rows of the matrix
    for i in range(n):
        # add the element at position (i, i) to diagonal1_sum
        diagonal1_sum += matrix[i][i]
        # add the element at position (i, n-i-1) to diagonal2_sum
        diagonal2_sum += matrix[i][n-i-1]

    # return the sum of the two diagonals
    return diagonal1_sum + diagonal2_sum
