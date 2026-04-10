class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        list2 = []
        for i in range(n):
            if(nums[i] in list2):
                return True
            else:
                list2.append(nums[i])
        return False