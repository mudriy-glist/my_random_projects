class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        if columnTitle is None:
            return None
        res = 0
        res_list = list(columnTitle)
        i = len(res_list) - 1
        for c in res_list:
            num = ord(c) - 64
            res += (num*(26**i))
            i -= 1       
        return res