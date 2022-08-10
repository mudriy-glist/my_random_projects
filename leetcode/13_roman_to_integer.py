class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = []
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        integer = 0

        for n in s:
            s_list.append(dict[n])
        i = 0   
        for l in s_list:
            try:
                if l < s_list[i+1]:
                    integer -= l
                else:
                    integer += l
            except:
                integer += l
            i += 1
        return integer