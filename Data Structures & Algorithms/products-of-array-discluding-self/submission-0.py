class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_no_zero = 1
        zero_pos = []
        output = []
        for i in range(len(nums)):
            if nums[i] != 0:
                prod_no_zero *= nums[i]
            else:
                zero_pos.append(i)
        if len(zero_pos) == 0:
            for i in range(len(nums)):
                output.append(int(prod_no_zero / nums[i]))
        elif len(zero_pos) == 1:
            output = [0 for i in range(len(nums))]
            output[zero_pos[0]] = prod_no_zero
        else:
            output = [0] * len(nums) 
        
        return output