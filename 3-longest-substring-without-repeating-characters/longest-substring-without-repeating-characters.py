class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_set = set()

        l = 0
        max_len = 0
        for r in range(len(s)):
            while s[r] in num_set:
                num_set.remove(s[l])
                l += 1

            max_len = max(max_len, r - l + 1)
            num_set.add(s[r])

        return max_len



        # max_len = 0
        # for i in range(len(s)):
        #     curr_len = 0
        #     seen = set()
        #     for j in range(i, len(s)):
        #         if s[j] not in seen:
        #             seen.add(s[j])
        #             curr_len += 1
        #             max_len = max(max_len, curr_len)
        #         else: 
        #             break
                
        # return max_len
                



