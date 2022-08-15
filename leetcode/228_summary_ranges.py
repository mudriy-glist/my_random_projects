def summaryRanges(nums):


    res = []
    start = None
    i = 0
    while i < len(nums): 
        if i > 0:
            if nums[i] - nums[i-1] > 1:
                if start != nums[i]:
                    res.append(str(start) + "->" + str(nums[i-1]))
                    start = nums[i]
                elif start == nums[i]:
                    res.append(str(nums[i]))
        if start is None:
            start = nums[i]
        if start == nums[i] and i == len(nums) - 1 or i == 0:
            res.append(str(nums[i]))
        i += 1
    return res


nums = [0,1,2,4,5,7]
var = summaryRanges(nums)
print(var)