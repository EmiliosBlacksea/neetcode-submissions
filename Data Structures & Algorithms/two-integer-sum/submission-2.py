class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_all = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if nums[i] in need_all:
                return [need_all[nums[i]],i]
            else:
                need_all[need] = i
        return 0