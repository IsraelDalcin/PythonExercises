""" ------------------------------------------DESCRIPTION-------------------------------------------------
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
----------------------------------------------------------------------------------------------------------
""" 

from collections import Counter

def scramble(s1, s2):
    if len(s2) > len(s1):
        return False
    
    contagem_letras1 = Counter(s1)
    contagem_letras2 = Counter(s2)
    
    for letra in contagem_letras2:
        if contagem_letras2[letra] > contagem_letras1.get(letra, 0):
            return False
    return True

# Helped and inspired by Giovanna Polissici's code