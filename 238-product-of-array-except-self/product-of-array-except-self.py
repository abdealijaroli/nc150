class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        
        # res = []

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             prod *= nums[j]
        #     res.append(prod)

        # return res


            