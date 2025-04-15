class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1 

        sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)

        return sorted_keys[:k]

