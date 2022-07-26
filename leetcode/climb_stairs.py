class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_num = 1
        second_num = 2
        num_of_terms = n
        if n == 1:
            return 1
        if n == 2:
            return 2
        while(num_of_terms-2):
            third_num = first_num + second_num
            first_num=second_num
            second_num=third_num
            num_of_terms=num_of_terms-1
        return third_num