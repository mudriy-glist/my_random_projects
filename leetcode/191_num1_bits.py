n = 0b1111101

def hammingWeight(n):
    i = 0
    while n:
        n = n & (n - 1)
        i += 1
    return i

var = hammingWeight(n)
print(var)