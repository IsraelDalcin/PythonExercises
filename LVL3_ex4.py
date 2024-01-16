""" ------------------------------------------DESCRIPTION-------------------------------------------------
Consider having a cow that gives a child every year from her fourth year of life on and all her subsequent children do the same.

After n years how many cows will you have?

countCows(0); // should equal 1
countCows(1); // should equal 1
countCows(3); // should equal 2
countCows(4); // should equal 3
countCows(10);// should equal 28
Return null if n is not an integer.

Note: Assume all the cows are alive after n years.
----------------------------------------------------------------------------------------------------------
""" 

class Vaca:
    def __init__(self, ano):
        self.ano = ano

def count_cows(n):
    if not isinstance(n, int):
        return None
    else:
        lista_vacas = []
        lista_vacas.append(Vaca(0))
        for ano in range(n+1):
            for vacas in lista_vacas:
                if ano - vacas.ano >= 3:
                    lista_vacas.append(Vaca(ano))
    return len(lista_vacas)