""" ------------------------------------------DESCRIPTION-------------------------------------------------
Triple Trouble
Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.
----------------------------------------------------------------------------------------------------------
""" 

def triple_trouble(one, two, three):
    nova_string1 = list(one)
    nova_string2 = list(two)
    nova_string3 = list(three)
    string_resultado = ''
    print(nova_string1, nova_string2, nova_string3)
    for i in range(len(one)):
        string_resultado += nova_string1[i] + nova_string2[i] + nova_string3[i]
    return string_resultado