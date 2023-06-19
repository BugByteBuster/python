def missingNums(nums):
    length = nums[-1] + 3
    #print(length)
    array = [i for i in range(1, length) if i not in nums]
    return (sorted(array))


missingNums([])