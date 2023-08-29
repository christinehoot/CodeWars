# Very simple, given an integer or a floating-point number, find its opposite.

def opposite(number):
    if number < 0:
        return abs(number)
    else:
        return 0 - number


# better solution
# def opposite(number):
#     return -number
