class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [] 
        for n in range(numRows):
            res.append([])
            res[n].append(1)
            for m in range(1, n):
                res[n].append(res[n - 1][m - 1] + res[n - 1][m])
            if(n != 0):
                res[n].append(1)
        return res