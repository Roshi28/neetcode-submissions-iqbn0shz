class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        final_ans = 0
        for i in range(n):
            if(nums[i] == 0):
                count = 0
            else:
                count = count + 1
            final_ans = max(final_ans, count)
        return final_ans