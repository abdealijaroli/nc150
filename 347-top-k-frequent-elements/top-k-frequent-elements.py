class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =[[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        for n, c in freq.items():
            count[c].append(n)

        res = []
        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                if len(res) != k:
                    res.append(n)
                    
        return res
        # res = []
        # freq = defaultdict(int)

        # for n in nums:
        #     freq[n] += 1 

        # sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)

        # return sorted_keys[:k]

