class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1count = {}
        s2count = {}

        for ch in s1:
            s1count[ch] = 1 + s1count.get(ch, 0)
        
        i, j = 0, 0
        while j < len(s2):
            while (j-i) < len(s1):
                s2count[s2[j]] = 1 + s2count.get(s2[j], 0)
                j += 1            
            
            if s1count == s2count:
                return True
            else:
                s2count[s2[i]] -= 1
                if s2count[s2[i]] == 0:
                    del s2count[s2[i]]

                i += 1
        
        return False
             




    # for j in range(i, len(s2)):
    #         if (j-i+1) == len(s1):
    #             s2count[i] = 1 + s2count.get(i, 0)           
    #             s2count[j] = 1 + s2count.get(j, 0)           

    #             if s1count == s2count:
    #                 return True
    #             else:
    #                 s2count[i] -= 1
    #                 s2count[j] -= 1
    #         else:
    #             i += 1

    #     return False