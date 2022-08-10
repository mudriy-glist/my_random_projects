class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        rem_list = ["()","[]","{}"]
        res = ""
        i = 0

        for i in range(len(s)):
            s = s.replace(rem_list[0], "")
            s = s.replace(rem_list[1], "")
            s = s.replace(rem_list[2], "")

        if s == "":
            return True
        else:
            return False