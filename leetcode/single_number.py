class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            i = len(nums) - 1
            num = nums.pop(i)
            if num in nums:
                nums.remove(num)
            elif num not in nums:
                return num
        return nums[0]