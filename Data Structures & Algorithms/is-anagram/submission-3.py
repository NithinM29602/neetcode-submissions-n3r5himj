class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_set = {}
        for each_char in s:
            char_set[each_char] = char_set.get(each_char, 0) + 1

        for each_char in t:
            char_set[each_char] = char_set.get(each_char, 0) - 1
        
        for each_value in char_set.keys():
            if char_set[each_value] != 0:
                return False
        return True

        