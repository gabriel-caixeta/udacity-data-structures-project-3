def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return (None, None)
    min_item = 9
    max_item = 0

    for item in ints:
        if item > max_item:
            max_item = item
        if item < min_item:
            min_item = item
    return (min_item, max_item)


def test_function(test_number, test_case, test_subject):
    min_max = get_min_max(test_case)
    expected = (min(test_case), max(test_case)) if test_case else (None, None)
    result = None
    if min_max == expected:
        result = "Pass"
    else:
        result = "Fail"
    print("{} - {} - {}".format(test_number, result, test_subject))

# Test 1 - empty array
test_function(1, [], "empty array") # (None, None)

# Test 2 - all the same
test_function(2, [5,5,5,5,5,5,5,5,5,5,5], "array of same number") # (5, 5)

# Test 3 - normal use cases
test_function(3, [6,7,4,5,0,9,1,3,4,7,8,9,5], "normal use case") # (0,9)
