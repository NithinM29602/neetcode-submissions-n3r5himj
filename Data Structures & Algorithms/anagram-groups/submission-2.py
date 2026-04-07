class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_set = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in freq_set: 
                freq_set[sorted_word] = []

            freq_set[sorted_word].append(word)

        return list(freq_set.values())