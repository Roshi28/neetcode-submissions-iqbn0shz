class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if(nums[i] == val):
                nums[i] = "_"
            else:
                k = k + 1

        while("_" in nums[0:k]):
            for i in range(n):
                if(nums[i] == "_"):
                    nums.pop(i)
                    nums.append("_")

        return k