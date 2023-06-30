#O(width * height)
def transposeMatrix(matrix):
    start_column = 0
    end_row = len(matrix)
    end_column = len(matrix[0])
    result = []

    for i in range(end_column):
        result.append([0 for j in range(end_row)])

    while start_column < end_column:
        for i in range(end_row):
            result[start_column][i] = matrix[i][start_column]
        start_column = start_column + 1

    return result
