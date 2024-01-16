""" ------------------------------------------DESCRIPTION-------------------------------------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
----------------------------------------------------------------------------------------------------------
""" 

def solution(number):
    lista_divisiveis_3 = []
    lista_divisiveis_5 = []
    if number < 0:
        return 0
    else:
        for contador in range(number):
            if contador % 3 == 0:
                lista_divisiveis_3.append(contador)
            if contador % 5 == 0:
                lista_divisiveis_5.append(contador)
            if contador % 3 == 0 and contador % 5 == 0:
                lista_divisiveis_5.pop()
        return sum(lista_divisiveis_3) + sum(lista_divisiveis_5)