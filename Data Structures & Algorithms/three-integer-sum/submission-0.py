class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, target):
            output = []
            needs = {}
            for i in range(len(nums)):
                if nums[i] in needs:
                    output.append([nums[i], nums[needs[nums[i]]]])
                needs[target - nums[i]] = i
            print(output)
            return output



        output = []
        hasbeen = set()
        for i in range(len(nums)):
            
            if nums[i] in hasbeen:
                continue
            else:
                print(nums[i])
                hasbeen.add(nums[i])
                temp = twoSum(nums[i + 1 : len(nums)], -nums[i])
                for j in range(len(temp)):
                    temp[j].append(nums[i])
                    temp[j].sort()
                    output.append(temp[j])
        if len(output) == 0:
            return output
        output.sort()
        final_output = []
        final_output.append(output[0])
        for i in range(1, len(output)):
            if output[i - 1] != output[i]:
                final_output.append(output[i])
        return final_output
        
