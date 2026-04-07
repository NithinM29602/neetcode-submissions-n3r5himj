class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for each_str in strs:
            sorted_str = ''.join(sorted(each_str))
            if sorted_str in result.keys():
                result[sorted_str].append(each_str)
                continue
            result[sorted_str] = [each_str]
        
        anagram_subsets = []
        for each_subset_key, each_subset_value in result.items():
            anagram_subsets.append(each_subset_value)
        return anagram_subsets