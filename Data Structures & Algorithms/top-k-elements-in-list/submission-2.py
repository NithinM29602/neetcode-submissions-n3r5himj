class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for e in nums:
            count[e] = 1 + count.get(e, 0)

        arr = []
        for value, cnt in count.items():
            arr.append([cnt, value])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result