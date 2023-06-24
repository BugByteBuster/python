def transposeMatrix(matrix):
    start_colum = 0
    end_rows = len(matrix)
    end_colums = len(matrix[0])

    result = []
    for i in range(end_colums):
        result.append([0 for j in range(end_rows)])

    while start_colum < end_colums:
        for i in range(end_rows):
            result[start_colum][i] = matrix[i][start_colum]
        start_colum = start_colum + 1
    return result


# one liner solution
def transpose_matrix(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


transposeMatrix(matrix=[[1, 2], [3, 4], [5, 6]])
transpose_matrix(matrix=[[1, 2], [3, 4], [5, 6]])
