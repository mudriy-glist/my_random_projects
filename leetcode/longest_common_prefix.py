# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = [""]
def long_pre(strs):
    common_prefix = ""
    
    shortest_item = min(strs, key=len)
    if strs == [""]:
        return common_prefix
    i = 0
    while i < len(shortest_item):
        first_letter_list =  [s[i] for s in strs]
        first_item = first_letter_list[0]
        for s in first_letter_list:
            if len(strs) == 1:
                return first_item
            elif s == first_item:
                continue
            else:
                return common_prefix
        common_prefix += first_item
        i += 1

var = long_pre(strs)
print(var)  
