""" ------------------------------------------DESCRIPTION-------------------------------------------------
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
----------------------------------------------------------------------------------------------------------
""" 

def spin_words(sentence):
    lista_palavras = sentence.split()
    print(lista_palavras)
    for contador,palavra in enumerate(lista_palavras):
        if len(palavra) >= 5:
            lista_palavras[contador] = palavra[::-1]
    sentence = ' '.join(lista_palavras)
    return sentence