class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l=len(nums)
        h={}
        for i in range(l):
            h[nums[i]] =h.get(nums[i],[])+[i]
        for v in h.values():
            if len(v)>1:
                for i in range(len(v)-1):
                    if abs(v[i]-v[i+1]) <= k:
                        return(True)
        return(False)