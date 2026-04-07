from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for each_str in strs:
            count = [0] * 26
            for s in each_str:
                count[ord(s) - ord('a')] += 1
            
            result[tuple(count)].append(each_str)
        
        return list(result.values())