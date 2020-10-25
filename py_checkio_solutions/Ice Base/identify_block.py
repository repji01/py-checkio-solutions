#!/home/mattie/.local/bin/checkio --domain=py run identify-block

# This mission uses a 4x4 grid. Each square is numbered from 1 to 16 in row-major order.
# You are given 4 numbers(a set of integers).These numbers represent the positions of each square on the grid and a whole block if all the squares are adjacent.
# 
# You have to identify the kind of block. (Refer to the following image or comment of initial code for the kind of block).
# The answer is an upper case alphabet letter ('I', 'J', 'L', 'O', 'S', 'T' or 'Z'). If it’s not a block, then return None.
# 
# The block is placed anywhere on the grid and can be rotated (0, 90, 180 or 270 degrees).
# 
# 
# 
# Input:4 numbers (a set of integers)
# 
# Output:the kind of block (an alphabet letter or         None)
# 
# 
# END_DESC

i_block = [tuple([1,2,3,4]),tuple([1,5,9,13])]
j_block = [tuple([2,6,9,10]),tuple([1,5,6,7]),tuple([1,2,3,7]),tuple([1,2,5,9])]
l_block = [tuple([1,5,9,10]),tuple([1,2,3,5]),tuple([1,2,6,10]),tuple([3,5,6,7])]
o_block = [tuple([1,2,5,6])]
s_block = [tuple([2,3,5,6]),tuple([1,5,6,10])]
t_block = [tuple([1,2,3,6]),tuple([2,5,6,10]),tuple([2,5,6,7]),tuple([1,5,6,9])]
z_block = [tuple([1,2,6,7]),tuple([2,5,6,9])]


def identify_block(numbers):
    """
    grid(4x4):
    +--+--+--+--+
    |1 |2 |3 |4 |
    +--+--+--+--+
    |5 |6 |7 |8 |
    +--+--+--+--+
    |9 |10|11|12|
    +--+--+--+--+
    |13|14|15|16|
    +--+--+--+--+


    blocks(7 kinds):

    'I'  'J'  'L'  'O'  'S'  'T'  'Z'

     *    *   *    **    **  ***  **
     *    *   *    **   **    *    **
     *   **   **
     *

    """
    numbers =sorted(numbers)
    #move up
    move = True
    while(move):
        for idx in range(0,4):
            if (move):
                move =not(numbers[idx]<5)
        if(move):
           for idx in range(0,4):
               numbers[idx] = numbers[idx]-4    
    #moveleft
    move = True
    while(move):
        for idx in range(0,4):
            if(move):
                 move = not(numbers[idx]%4==1)
        if(move):
            for idx in range(0,4):
                numbers[idx] = numbers[idx]-1   
    print(numbers)
    if (tuple(numbers) in i_block):
        return 'I'
    if (tuple(numbers) in j_block):
        return 'J'    
    if (tuple(numbers) in t_block):
        return 'T' 
    if (tuple(numbers) in l_block):
        return 'L' 
    if (tuple(numbers) in o_block):
        return 'O'
    if (tuple(numbers) in s_block):
        return 'S'
    if (tuple(numbers) in t_block):
        return 'T'
    if (tuple(numbers) in z_block):
        return 'Z'      
    return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
   
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2,3,7,11}) == 'L', 'L'
    assert identify_block({ 2, 3, 4,8}) == 'J', 'J'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')
