#!/home/mattie/.local/bin/checkio --domain=py run gcd

# "[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm        that has survived to the present day."
# -- Donald Knuth, The Art of Computer Programming, Vol. 2: Seminumerical Algorithms, 2nd edition (1981).
# 
# The greatest common divisor(GCD), also known as    the greatest common factor of two or more integers (at least one of which is not zero), is the largest positive    integer that divides a number without a remainder. For example, the GCD of 8 and 12 is 4.
# 
# You are given an arbitrary number of positive integers.    You should find the greatest common divisor for these numbers.
# 
# Input:An arbitrary number of positive integers.
# 
# Output:The greatest common divisor as an integer.
# 
# Example:
# 
# 
# great_common_divisor(6, 4) == 2
# great_common_divisor(2, 4, 8) == 2
# Precondition:
# 1 < len(args) ≤ 10
# all(0 < x ≤ 2 ** 32 for x in args)
# END_DESC

def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    res = args[0]
    for c in args[1::]:
        res = gcd(res , c)
    return res

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"