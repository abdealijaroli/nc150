class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)

        max_length = 1
        for num in s:
            if (num - 1) not in s:       # means it is the starting point of the chain
                length = 1
                while (num + length) in s:
                    length += 1
                
                max_length = max(max_length, length) 
            
        return max_length

        
        ####################################
        # if not nums:
        #     return 0
    
        # nums = sorted(set(nums))

        # max_len = 1
        # curr_len = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         curr_len += 1
        #         max_len = max(max_len, curr_len)
        #     else:
        #         curr_len = 1
        
        # return max_len
            