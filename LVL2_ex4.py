""" ------------------------------------------DESCRIPTION-------------------------------------------------
You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.
----------------------------------------------------------------------------------------------------------
""" 

def small_enough(array, limit):
    count = 0
    for i in array:
        if i <= limit:
            count += 1
    if count == len(array):
        return True
    else:
        return False