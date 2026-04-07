class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dupNums = nums[:]
        for index, eachNum in enumerate(dupNums):
            values = dupNums[:index] + dupNums[index + 1:]
            total = 1
            for eachValue in values:
                total *= eachValue
			
            nums[index] = total
        return nums
        