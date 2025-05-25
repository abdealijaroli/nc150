class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            curr_len = 0
            seen = set()
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    curr_len += 1
                    max_len = max(max_len, curr_len)
                else: 
                    break
                
        return max_len
                


        # num_set = set()

        # l = 0

        # for r in range(len(s)):
        #     if s[r] in num_set:
        #         num_set.remove(s[l])


        #     num_set.add(s[r])


