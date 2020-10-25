#!/home/mattie/.local/bin/checkio --domain=py run reverse-roman-numerals

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }In the CheckiO missionRoman Numeralsyou have to convert a decimal    number into its representation as a roman number.
# Here you have to do the same but the other way around.
# 
# You are given a Roman number as a string and your job is to convert this number into  its decimal representation.
# 
# A valid Roman number, in the context of this mission, will only  contain Roman numerals as per the below tableandfollow the rules of  the subtractive notation.
# Check thisWikipedia articleout for more details on how to form Roman numerals.NumeralValueI1 (unus)V5 (quinque)X10 (decem)L50 (quinquaginta)C100 (centum)D500 (quingenti)M1,000 (mille)
# 
# Input:A roman number as a string.
# 
# Output:The decimal representation of the roman number as an int.
# 
# Precondition:
# len(roman_string) > 0
# all(char in "MDCLXVI" for char in roman_string) == True
# 0 < reverse_roman(roman_string) < 4000
# 
# 
# 
# END_DESC

numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'D', 'value': 500},
        {'letter': 'C', 'value': 100},
        {'letter': 'L', 'value': 50},
        {'letter': 'X', 'value': 10},
        {'letter': 'V', 'value': 5},
        {'letter': 'I', 'value': 1},
    ]

def reverse_roman(roman_string):

    index_by_letter = {}
    for index in range(len(numerals)):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(roman_string):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value

    return result
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');