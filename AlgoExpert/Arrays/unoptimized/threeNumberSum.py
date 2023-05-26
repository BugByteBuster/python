#O(n) == O(n^3)
def threeNumberSum(array, targetSum):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                combination = [arr[i], arr[j], arr[k]]
                if sum(result) == targetSum:
                    result.append(sort(combination))
    return result
