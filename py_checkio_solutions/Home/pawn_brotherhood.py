#!/home/mattie/.local/bin/checkio --domain=py run pawn-brotherhood

# 
# END_DESC

import string
from collections import Counter

def safe_pawns(pawns):
    return  len(Counter(pawn for pawn in pawns if((chr(ord(pawn[0])-1)+'{}'.format(int(pawn[1])-1) in pawns)|(chr(ord(pawn[0])+1)+'{}'.format(int(pawn[1])-1) in pawns))).items())

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
  #  assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")