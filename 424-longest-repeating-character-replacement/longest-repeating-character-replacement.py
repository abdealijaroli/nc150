class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0                                    #optimized
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])           #optimized

            # if (r-l+1) - max(count.values()) > k:  
            if (r-l+1) - maxf > k:                  #optimized
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res