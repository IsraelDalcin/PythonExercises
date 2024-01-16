""" ------------------------------------------DESCRIPTION-------------------------------------------------
We know the formula to find the solutions of an equation of second degree with only one variable:
We need the function sec_deg_solver()/secDegSolver(), that accepts three arguments, a, b and c, the coefficients of the above equation.

The outputs of the function may vary depending on the values of coefficients a, b and c, according to the following situations. (used values as examples only):


- If a is equal 0:
                  - If b and c are not 0. It will return: "It is a 
                    first degree equation. Solution: 0.5512345"
   
                  - If a, b and c are 0. It will return: 
                     "The equation is indeterminate"
           
                  - If a and b are 0, and c is not 0. It will 
                     return: "Impossible situation. Wrong entries"
                  
                  - If a and c are 0 and b is not 0: It will return: "It is a first 
                    degree equation. Solution: 0.0"

- If a is not 0:
                  - If Δ < 0 (see image above). It will return: "There are no real 
                    solutions"

                  - If Δ = 0. It will return: "It has one double solution: 
                    1.4142135624"

                  - If Δ > 0. It will return: "Two solutions: 1,7320508076, 2.0"
                    (solutions should be sorted)
The results should be expressed up to 10 decimals rounded result Let's see some cases:


a = 0
b = 2
c = -4
sec_deg_solver(a, b, c) == It is a first degree equation. Solution: 2.0

a = 10
b = 2
c = -4
sec_deg_solver(a, b, c) == Two solutions: -0.7403124237, 0.5403124237

a = 1.5
b = 2
c = 4
sec_deg_solver(a, b, c) == There are no real solutions

a = 1
b = -2
c = 1
sec_deg_solver(a, b, c) == It has one double solution: 1.0

a = 0
b = 0
c = 0
sec_deg_solver(a, b, c) == The equation is indeterminate
(Be aware that the result has a string format and -0.0 is not 0.0)

Note on having two solutions: input them sorted numerically; in the JavaScript version, not to put any extra difficulty on this one, sort them with a simple .sort() (which will sort them lexicographically).

Happy coding!!
----------------------------------------------------------------------------------------------------------
""" 

import math
from decimal import Decimal
def sec_deg_solver(a, b, c):
    solucoes = list()
    if a == 0:
        if b != 0 and c != 0:
            calculo_primeiro_grau = (Decimal(f'{float(-(c / b)):.10f}').normalize())
            if '.' not in str(calculo_primeiro_grau):
                calculo_primeiro_grau = float(f'{calculo_primeiro_grau:.1f}')
            return(f'It is a first degree equation. Solution: {calculo_primeiro_grau}')
        if b == 0 and c == 0:
            return('The equation is indeterminate')
        if b == 0 and c != 0:
            return('Impossible situation. Wrong entries')
        if c == 0 and b != 0:
            return('It is a first degree equation. Solution: 0.0')
    if a != 0:
        delta = 0
        x1 = 0
        x2 = 0
        delta = (b ** 2) - 4 * a * c
        if delta < 0:
            return('There are no real solutions')
        if delta > 0:
            delta_raiz = math.sqrt(delta)
            x1 = (-1*b + delta_raiz) / (2*a)
            x2 = (-1*b - delta_raiz) / (2*a)
            if abs(x1) == 0:
                x1 = 0
            if abs(x2) == 0:
                x2 = 0
            solucoes.append(Decimal(f'{x1:.10f}').normalize())
            solucoes.append(Decimal(f'{x2:.10f}').normalize())
            if '.' not in str(solucoes[0]):
                solucoes[0] = float(f'{x1:.1f}')
            if '.' not in str(solucoes[1]):
                solucoes[1] = float(f'{x2:.1f}')
            solucoes.sort()
            return(f'Two solutions: {solucoes[0]}, {solucoes[1]}')
        if delta == 0:
            x1 = (-1*b + (delta**0.5)) / (2*a)
            return(f'It has one double solution: {x1:.1f}')