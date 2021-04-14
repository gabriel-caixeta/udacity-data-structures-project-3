import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return sqrt_auxiliary(number, 0, number)


def sqrt_auxiliary(number, start, end):
    if start > end:
        return None
    if start == end:
        start_sqr = start * start
        return (start) if start_sqr <= number else (start - 1)

    guess = (end + start) // 2 + 1
    guess_sqr = guess * guess

    if guess_sqr == number:
        return guess
    if guess_sqr < number:
        return sqrt_auxiliary(number, guess, end)
    else:
        return sqrt_auxiliary(number, start, guess-1)


# Tests - run tests from 0 - 100 and print "{number} - Pass" if successful, or "{number} - Fail" if not
for i in range(101):
    result = ""
    if (sqrt(i) == math.floor(math.sqrt(i))):
        result = "Pass"
    else:
        result = "Fail"
    print("{} - {}".format(i, result))


