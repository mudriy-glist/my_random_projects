class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        i = 0
        for num in nums:
            if nums[i - 1] == num and len(nums) > 1:
                nums[i - 1] = "_"
            i += 1
        under_score = 0
        while "_" in nums:
            for num in nums:
                if num == "_":
                    nums.remove(num)
                    under_score += 1
        k -= under_score
        print(k, nums)