class Solution:
    def twoNumberSum(self, array, targetSum):
        num_set = set(array)
        for num in num_set:
            difference = targetSum - num
            if difference in array and difference != num:
                return [num, difference]
        return []

solution = Solution()
#testcase-1
print(solution.twoNumberSum(array=[3, 5, -4, 8, 11, 1, -1, 6], targetSum=10))