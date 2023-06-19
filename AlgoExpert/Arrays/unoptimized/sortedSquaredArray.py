def sortedSquaredArray(array):
    multiplier = 0
    result = []
    while multiplier < len(array):
        result.append(array[multiplier] * array[multiplier])
        multiplier = multiplier + 1
    return sorted(result)


sortedSquaredArray([1, 2, 3, 5, 6, 8, 9])
