class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [] 
        for n in range(rowIndex + 1):
            res.append([])
            res[n].append(1)
            for m in range(1, n):
                res[n].append(res[n - 1][m - 1] + res[n - 1][m])
            if(n != 0):
                res[n].append(1)
        return res[rowIndex]