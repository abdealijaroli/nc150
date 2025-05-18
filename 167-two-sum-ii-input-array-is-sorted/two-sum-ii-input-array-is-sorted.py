class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        
        ############################################
        # res = [0, 0]
        # i, j = 0, 1

        # while i < len(numbers):
        #     if j < len(numbers):
        #         if numbers[j] == target - numbers[i]:
        #             res[0] = i + 1  # 1-based index
        #             res[1] = j + 1
        #             break
        #         j += 1
        #     else:
        #         i += 1
        #         j = i + 1
                
        # return res