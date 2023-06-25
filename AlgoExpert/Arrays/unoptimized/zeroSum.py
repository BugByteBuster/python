def zeroSumSubarray(arr):
    sums = set([0])
    currentSum = 0
    for num in arr:
        currentSum = currentSum + num
        if currentSum in sums:
            return True
        sums.add(currentSum)
    return False
