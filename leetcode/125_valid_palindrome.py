class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True

        new_s = ''.join(c for c in s if c.isalnum())
        new_s = new_s.lower()
        res_list = []
        for i in new_s:
            res_list.append(i)

        if res_list == res_list[::-1] or len(res_list) == 1:
            return True
        elif res_list != res_list[::-1]:
            return False