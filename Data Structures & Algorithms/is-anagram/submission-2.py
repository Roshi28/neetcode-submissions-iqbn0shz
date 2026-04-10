class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        p = ord('a')
        list1 = [0] * 26
        list2 = [0] * 26
        for i in range(n):
            list1[ord(s[i]) - ord('a')] = list1[ord(s[i]) - ord('a')] + 1
        for j in range(m):
            list2[ord(t[j]) - ord('a')] = list2[ord(t[j]) - ord('a')] + 1

        if(list1 == list2):
            return True
        else:
            return False