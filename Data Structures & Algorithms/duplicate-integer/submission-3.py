class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for each_num in nums:
            if each_num in uniqueSet:
                return True
            else:
                uniqueSet.add(each_num)
            
        return False

        