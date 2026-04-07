class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for each_value in set(nums):
            count = nums.count(each_value)
            frequency[each_value] = count

        sorted_frequency = dict(sorted(frequency.items(), reverse=True, key=lambda kv: (kv[1], kv[0])))
        sorted_keys = list(sorted_frequency.keys())
        return sorted_keys[:k]

        