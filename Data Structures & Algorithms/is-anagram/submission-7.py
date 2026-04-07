class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_freq = dict()

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for char in t:
            if char not in char_freq:
                return False
            
            char_freq[char] = char_freq.get(char, 0) - 1
            
            if char_freq[char] < 0:
                return False
            
        return True