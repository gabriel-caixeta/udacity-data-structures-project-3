import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return None
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


def test_function(number):
    if number is None:
        expected = None
    else:
        expected = math.floor(math.sqrt(number)) if number >= 0 else None
    result = ""

    if sqrt(number) == expected:
        result += "Pass"
    else:
        result += "Fail"
    print("{} - {}".format(number, result))

# Edge case #1 - null
test_function(None)

# Edge case #2 - negative
test_function(-1)

# Edge case #3 - zero
test_function(0)

# Edge case #4 - decimal
test_function(0.1)

# Tests - run tests from 1 - 100 and print "{number} - Pass" if successful, or "{number} - Fail" if not
for i in range(1, 101):
    test_function(i)
