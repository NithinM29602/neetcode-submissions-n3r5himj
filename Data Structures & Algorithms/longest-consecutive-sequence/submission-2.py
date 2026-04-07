class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNum = set(nums)
        
        longest = 0
        for eachNum in uniqueNum:
            countStreak = 0
            if eachNum-1 not in uniqueNum:
                countStreak = 1
                nextElement = eachNum + 1
                while True:
                    if nextElement in uniqueNum:
                        countStreak += 1
                        nextElement += 1
                        continue
                    else:
                        break
            
            if countStreak > longest:
                longest = countStreak
        
        return longest


        
