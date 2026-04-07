class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for num in nums:
            streak, cur = 0, num
            while cur in store:
                streak += 1
                cur += 1

            res = max(streak, res)

        return res
                


        
        