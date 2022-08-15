class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s and t is None:
            return True
        s_map = {}
        t_map =  {}
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1   
        s_list = []
        t_list = []
        for k in s_map:
            val = s_map[k]
            s_list.append(val)
        for k in t_map:
            val = t_map[k]
            t_list.append(val)
        return s_list == t_list



#Super solutionxD
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.find,s)) == list(map(t.find,t))