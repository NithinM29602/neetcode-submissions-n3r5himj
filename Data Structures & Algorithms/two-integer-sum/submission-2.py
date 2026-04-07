class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum_map = {}
        for index, each_num in enumerate(nums):
            value = target - each_num
            if value in two_sum_map:
                return [two_sum_map[value], index]
            
            two_sum_map[each_num] = index
            
        return []
        