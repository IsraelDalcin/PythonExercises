""" ------------------------------------------DESCRIPTION-------------------------------------------------
Build a function that will take the length of each side of a triangle and return if it's either an Equilateral, an Isosceles, a Scalene or an invalid triangle.

It has to return a string with the type of triangle.
For example:

type_of_triangle(2, 2, 1) --> "Isosceles"
----------------------------------------------------------------------------------------------------------
""" 

MSG = {
    0: 'Equilateral', 
    1: 'Scalene', 
    2: 'Isosceles',
    3: 'Not a valid triangle'
}
def type_of_triangle(a, b, c):
    print(a,b,c)
    if str(a).isnumeric() and str(b).isnumeric() and str(c).isnumeric():
        if abs(b - c) < a < b + c:
            if a == b and a == c and b == c:
                msg = MSG[0]
            elif a != b and a != c and b != c:
                msg = MSG[1]
            elif a == b or a == c or b == c:
                msg = MSG[2]
        else:
            msg = MSG[3]
    else:
        msg = MSG[3]
    return msg