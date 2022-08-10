class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        
        map = {}
        for i in range(0, len(nums)):
            if nums[i] in map.keys():
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        for key in map:
            if map[key] > (len(nums) / 2):
                return key
        return None