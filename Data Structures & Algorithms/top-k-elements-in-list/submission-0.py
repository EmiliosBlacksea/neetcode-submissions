class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = [[] for i in range(len(nums) + 1)]
        for number in nums:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        for i in count:
            result[count[i]].append(i)
        output = []
        c = 0
        for i in reversed(range(len(result))):
            for n in result[i]:
                output.append(n)
                c += 1
                if c == k:
                    return output

        return 0
