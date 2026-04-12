class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sum = 0
        list = []
        for i in range(n):
            for j in range(n):
                sum = nums[i] + nums[j]
                if((sum == target) and (i != j)):
                    list.append(i)
                    list.append(j)
                    return list