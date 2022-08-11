class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        while True:
            sum = 0
            while n != 0:
                #if 19 / 10, remainder will be 9 and so on, it's how we separate digits 
                rem = n % 10
                sqr = rem*rem
                sum = sum + sqr
                #19 / 10 = 1.9, then int will round it to 1, it's how we get second number
                n = int(n/10)
            #basically a task
            if sum == 1:
                return True
            #if numbers are unhappy they will be in eternal cycle of 4, 16, 37, 58, 89, 145 and so on,
            #idk why, if someone can explain I will appreciate it
            elif sum == 4 or sum == 16:
                return False
            #to keep a cycle running
            n = sum