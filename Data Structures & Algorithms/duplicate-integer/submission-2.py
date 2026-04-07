class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hased_set = set()
        for each_value in nums:
            if each_value in hased_set:
                return True
            hased_set.add(each_value)
        return False