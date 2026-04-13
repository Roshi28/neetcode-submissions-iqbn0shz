class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagrams(x, y):
            list1 = [0] * 26
            list2 = [0] * 26
            n = len(x)
            m = len(y)
            count = 0
            for i in range(n):
                list1[ord(x[i]) - ord('a')] = list1[ord(x[i]) - ord('a')] + 1

            for j in range(m):
                list2[ord(y[j]) - ord('a')] = list2[ord(y[j]) - ord('a')] + 1

            if (list1 == list2):
                return True
            return False

        list = []
        p = len(strs)
        count = [0] * p
        for i in range(p):
            if(count[i] == 1):
                continue
            temp = []
            temp.append(strs[i])
            j = i + 1
            while (j < p):
                if(anagrams(strs[j], strs[i])):
                    if(count[j] == 1):
                        continue
                    temp.append(strs[j])
                    count[j] = count[j] + 1
                j += 1
            list.append(temp)
        return list