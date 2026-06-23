class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        record = []
        sum = 0

        for i in range(n):
            if(operations[i] == "C"):
                record.pop()
            elif(operations[i] == "+"):
                record.append(int(record[-1] + record[-2]))
            elif(operations[i] == "D"):
                record.append(2 * int(record[-1]))
            else:
                record.append(int(operations[i]))
        for j in range(len(record)):
            sum = sum + record[j]
        return sum