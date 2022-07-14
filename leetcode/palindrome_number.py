class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        xr = "".join(reversed(str(x)))
        if x == xr:
            return True
        else:
            return False