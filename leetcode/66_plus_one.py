class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string_digits = [str(i) for i in digits]
        integers = int("".join(string_digits))
        res = str(integers + 1)
        digits_list = []
        for i in res:
            digits_list.append(i)

        return digits_list