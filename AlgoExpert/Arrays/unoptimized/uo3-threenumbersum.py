def threeNumberSum(array, targetSum):
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            complement = targetSum - (array[i] + array[j])
            if (
                complement in array[j + 1 :]
                and [array[i], array[j], complement] not in result
            ):
                result.append(sorted([array[i], array[j], complement]))
    return sorted(result)
