#!/home/mattie/.local/bin/checkio --domain=py run bird-language

# Stephan has a friend who happens to be a little mechbird.    Recently, he was trying to teach it how to speak basic language.    Today the bird spoke its first word: "hieeelalaooo".    This sounds a lot like "hello", but with too many vowels.    Stephan asked Nikola for help and he helped to examine how the bird changes words.    With the information they discovered, we should help them to make a translation module.
# 
# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);Vowels letters == "aeiouy".
# You are given an ornithological phrase as several words which are separated by white-spaces    (each pair of words by one whitespace).    The bird does not know how to punctuate its phrases and only speaks words as letters.    All words are given in lowercase.    You should translate this phrase from the bird language to something more understandable.
# 
# Input:A bird phrase as a string.
# 
# Output:The translation as a string.
# 
# Precondition:re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# A phrase always has the translation.
# 
# 
# END_DESC

import string
VOWELS = "aeiouy"

def translate(phrase):
    chars = ''.join(c for c in string.ascii_lowercase if c not in VOWELS)
    idx = 0
    ss =''
    while(idx<len(phrase)):
        if(phrase[idx] in chars):
            ss=ss+phrase[idx]  
            idx=idx+1            
        elif(phrase[idx] in VOWELS):
            ss=ss+phrase[idx]
            idx=idx+2
        else:
            ss=ss+phrase[idx]
        idx=idx+1
    return ss

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"