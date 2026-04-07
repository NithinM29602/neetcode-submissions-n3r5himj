class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            char_freq = [0] * 26
            for char in word:
                char_freq[ord(char) - ord('a')] += 1

            key = tuple(char_freq)
            if key not in groups:
                groups[tuple(char_freq)] = []
            
            groups[tuple(char_freq)].append(word)
        
        return list(groups.values())
