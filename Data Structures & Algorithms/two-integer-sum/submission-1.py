class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for idx, each_value in enumerate(nums):
            rem_portion = target - each_value
            if rem_portion in result.keys():
                return [result[rem_portion], idx]
            else:
                result[each_value] = idx

                
        