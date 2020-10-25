#!/home/mattie/.local/bin/checkio --domain=py run hamming-distance2

# The Hamming distance between two binary integers is the number of bit positions that differs    (read more about the Hamming distance on Wikipedia).    For example:
# 
# 
#     117 = 0 1 1 1 0 1 0 1
#      17 = 0 0 0 1 0 0 0 1
#       H = 0+1+1+0+0+1+0+0 = 3
# 
# You are given two positive numbers (N, M) in decimal form.    You should calculate the Hamming distance between these two numbers in binary form.
# 
# Input:Two arguments as integers.
# 
# Output:The Hamming distance as an integer.
# 
# Precondition:
# 0 < n < 106
# 0 < m < 106
# 
# 
# 
# END_DESC

def checkio(n, m):
    m_str = "{:020b}".format(m)
    n_str = "{:020b}".format(n)
    return sum(int(m_str[x] != n_str[x]) for x in range(0,len(n_str)) if m_str[x] != n_str[x])
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"