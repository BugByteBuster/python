def threeNumberSum(array, targetSum):
    result = []
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                combination = [array[i], array[j], array[k]]
                if sum(combination) == targetSum:
                    result.append(sorted(combination))
    print(sorted(result))

threeNumberSum(array=[12, 3, 1, 2, -6, 5, -8, 6], targetSum=8)