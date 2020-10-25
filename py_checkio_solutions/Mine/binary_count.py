#!/home/mattie/.local/bin/checkio --domain=py run binary-count

# 
# END_DESC

def checkio(number):
    return sum(int(x) for x in bin(number) if (x == "1"))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9