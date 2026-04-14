class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list = []
        n = len(nums)
        for i in range(n):
            if (nums[i] not in list):
                list.append(nums[i])
        m = len(list)
        count = [0] * m
        for i in range(n):
            for j in range(m):
                if(nums[i] == list[j]):
                    count[j] = count[j] + 1
        final_list = []
        while k != 0:
            max_ind = count.index(max(count))
            final_list.append(list[max_ind])
            count.pop(max_ind)
            list.pop(max_ind)
            k = k - 1
        return final_list