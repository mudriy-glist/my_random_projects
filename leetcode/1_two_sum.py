nums = [2,7,11,15]
target = 9

def TwoSums(nums, target):
    i = 0
    while i < len(nums):
        counter = 0
        for num in nums:
            if nums[i] + num == target and nums[i] != counter:      
                result = [i,counter]
                return result 
            counter += 1    # return result
        i += 1