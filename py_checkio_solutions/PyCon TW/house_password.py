#!/home/mattie/.local/bin/checkio --domain=py run house-password

# 
# END_DESC

def checkio(data):

    #replace this for solution
    letters = set(data)
    return any(letter.islower() for letter in letters) and any(letter.isupper() for letter in letters) and any(letter.isdigit() for letter in letters) and (len(data) > 9)
    

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")