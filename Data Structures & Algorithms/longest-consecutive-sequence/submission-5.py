class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        max_count = 0
        for num in nums:
            if num not in seq:
                if num - 1 in seq: #num - 1 is the xth element of a sequence
                    beg_seq = num - seq[num - 1]
                    seq[beg_seq] += 1
                    seq[num] = seq[beg_seq]
                    if num + 1 in seq:
                        end_seq = num + seq[num + 1]
                        seq[end_seq] += seq[beg_seq]
                        seq[beg_seq] = seq[end_seq]
                elif num + 1 in seq:
                    beg_seq = num
                    end_seq = num + seq[num + 1]
                    seq[end_seq] += 1
                    seq[beg_seq] = seq[end_seq]
                else:
                    seq[num] = 1
                
        for count in seq:
            max_count = max(seq[count], max_count)
        return max_count
            
