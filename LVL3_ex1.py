""" ------------------------------------------DESCRIPTION-------------------------------------------------
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
----------------------------------------------------------------------------------------------------------
""" 

def what_century(year):
    print(year)
    splitado = [*year]
    ano = ''
    posicao1 = 0
    posicao2 = 0
    sufixo = ''
    for c, i in enumerate(splitado): 
        if c == 0:
            posicao1 = int(i)
        if c == 1:
            posicao2 = int(i)+1
            
    if splitado[1] == '9':
        posicao2 = 0
        posicao1 = int(splitado[0]) + 1
    if splitado[2] == '9' and splitado[3] == '9' and splitado[1] == '9':
        posicao2 = 0
        posicao1 = int(splitado[0]) + 1
    if splitado[1] == '9':
                posicao2 = 0
                posicao1 = int(splitado[0]) + 1
                if splitado[2] == '0' and splitado[3] == '0':
                    posicao2 = int(splitado[1])
                    posicao1 = int(splitado[0])
    if splitado[2] == '0' and splitado[3] == '0' and splitado[1] != '9':
        posicao2 = int(posicao2 - 1)
        if posicao2 < 0:
            posicao2 = 0
    ano = str(posicao1) + str(posicao2)
    print(ano)
    if int(ano) <= 3:
        if posicao2 == 1:
            sufixo = 'st'
        if posicao2 == 2:
            sufixo = 'nd'
        if posicao2 == 3:
            sufixo = 'rd'
    elif 3 < int(ano) < 21:
        sufixo = 'th'
    else:
        if posicao2 == 0:
            sufixo = 'th'
        if posicao2 == 1:
            sufixo = 'st'
        if posicao2 == 2:
            sufixo = 'nd'
        if posicao2 == 3:
            sufixo = 'rd'
        if posicao2 > 3:
            sufixo = 'th'
    ano = str(posicao1) + str(posicao2) + sufixo
    return ano