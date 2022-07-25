class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        while val in nums:
            for num in nums:
                if num == val:
                    nums.remove(num)
                    i += 1

        print(i, nums)


