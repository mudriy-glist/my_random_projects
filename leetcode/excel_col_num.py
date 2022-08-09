class Solution(object):
    def convertToTitle(self, columnNumber):
        
        
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while columnNumber >0:
            res += alpha[(columnNumber-1)%len(alpha)]
            columnNumber = (columnNumber-1)//len(alpha)
        return res[::-1]