class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for idx, value in enumerate(nums):
            mult_result = 1
            for j in nums[:idx]+nums[idx+1:]:
                mult_result *= j
            results.append(mult_result)
        return results
        