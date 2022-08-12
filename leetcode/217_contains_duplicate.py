class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_map = {}
        for l in nums:
            if l in nums_map:
                nums_map[l] += 1
            else:
                nums_map[l] = 1
        for k in nums_map.keys():
            if nums_map[k] > 1:
                return True
        return False