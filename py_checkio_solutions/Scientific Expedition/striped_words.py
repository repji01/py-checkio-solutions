#!/home/mattie/.local/bin/checkio --domain=py run striped-words

# Our robots are always working to improve their linguistic skills.    For this mission, they research the Latin alphabet and its applications.
# 
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels --A E I O U Y
# Consonants --B C D F G H J K L M N P Q R S T V W X Z
# 
# You are given a block of text with different words.     These words are separated by whitespaces and punctuation marks.    Numbers are not considered as words in this mission (a mix of letters and digits is not a word either).    You should count the number of words (striped words) where the vowels with consonants are alternating;     words that you count cannot have two consecutive vowels or consonants.    The words consisting of a single letter are not striped -- don't count those. Casing is not significant for this mission.
# 
# Input:A text as a string (unicode)
# 
# Output:A quantity of striped words as an integer.
# 
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105
# 
# 
# END_DESC

import re


def checkio(text): 
    VOWELS = "AEIOUY"
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
    VOWELS = VOWELS + VOWELS.lower()
    CONSONANTS = CONSONANTS + CONSONANTS.lower()
    words = list(filter(lambda w: w != "" and len(w) > 1 and w.isalpha(), re.split("\W",text)))
    counter = len(words)
    for w in words:
        for p , n in zip(w,w[1:]):
            if ( p in VOWELS and n in VOWELS ) or ( p in CONSONANTS and n in CONSONANTS ):
                counter -= 1
                break

    return counter

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"