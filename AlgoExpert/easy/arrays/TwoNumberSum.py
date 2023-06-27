#o(n) time complexity
def twoNumberSum(array, targetSum):
    uniqueNumbers = set(array)
    for firstNumber in uniqueNumbers:
        secondNumber = targetSum - firstNumber
        if secondNumber in uniqueNumbers and secondNumber != firstNumber:
            return [firstNumber, secondNumber]
    return []


twoNumberSum(array=[3, 5, -4, 8, 11, 1, -1, 6], targetSum=2)
