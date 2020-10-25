#!/home/mattie/.local/bin/checkio --domain=py run stressful-subject

# 
# END_DESC

red_words = {"HELP","ASAP","URGENT"}
def is_stressful(subj):
    """
        recoognise stressful subject
    """
    if (subj.isupper()) or (subj.endswith("!!!")):
        return True
        
    excl = lambda attr,char: ''.join([x+ char for x in attr])[:-1]
    removed = lambda attr:''.join(['' if i>0 and e==attr[i-1] else e for i,e in enumerate(attr)])
    
    subj = (removed(subj.upper()))
    
    for word in red_words:
        if (subj.find(word) != -1) or (subj.find(excl(word,"!")) != -1) or (subj.find(excl(word,"-")) != -1)or (subj.find(excl(word,".")) != -1):
            return True
    
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert True,"hh"
    print('Done! Go Check it!')