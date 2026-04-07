class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_duplicate = {}
        for each_value in nums:
            if each_value not in test_duplicate.keys():
                test_duplicate[each_value] = True
            else:
                return True
        return False