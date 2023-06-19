def twoNumberSum(array, targetSum):
    nums = set()
    for num in array:
        diff = targetSum - num
        if diff in nums and diff != num:
            return [diff, num]
        nums.add(num)
    return []