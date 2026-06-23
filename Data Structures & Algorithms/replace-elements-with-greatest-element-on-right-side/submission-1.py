class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(0,n-1):
            arr[i] = max(arr[i+1::])
        arr[-1] = -1
        return arr