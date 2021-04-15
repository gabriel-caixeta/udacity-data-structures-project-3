def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    rotation_index = find_rotation_point(input_list, 0, len(input_list) - 1)

    # array is not rotated
    # return normal binary search on the whole array
    if rotation_index == -1:
        return binary_search(input_list, 0, len(input_list)-1, number)

    # array is rotated
    # do binary search on the first non-rotated half
    # if `number` was not found, do binary search on the second non-rotated half
    search_result = binary_search(input_list, 0, rotation_index, number)
    if search_result == -1:
        search_result = binary_search(input_list, rotation_index + 1, len(input_list) - 1, number)
    return search_result

def find_rotation_point(input_list, start, end):
    if end < start: 
        return -1
    # rotation point found
    if start == end:
        return start
    middle = (start + end) // 2
    # rotation point is in the vicinity of `middle`
    if (middle < end) and (input_list[middle] > input_list[middle + 1]):
        return middle
    if (middle > start) and (input_list[middle] < input_list[middle - 1]):
        return middle - 1
    # array is rotated before `middle`
    if input_list[start] >= input_list[middle]:
        return find_rotation_point(input_list, start, middle - 1)
    # array is non-rotated until `middle`
    return find_rotation_point(input_list, middle + 1, end)

def binary_search(input_list, start, end, number):
    if end < start:
        return -1
    if start == end:
        if input_list[start] == number:
            return start
        return -1

    middle = (start + end) // 2
    middle_item = input_list[middle]

    if middle_item == number:
        return middle
    if middle_item > number:
        return binary_search(input_list, start, middle - 1, number)
    return binary_search(input_list, middle + 1, end, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_number, test_case, test_subject):
    input_list = test_case[0]
    number = test_case[1]
    result = None
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        result = "Pass"
    else:
        result = "Fail"
    print("{} - {} - {}".format(test_number, result, test_subject))

test_function(1, [[], 1], "empty array")
test_function(2, [[6, 7, 8, 1, 2, 3, 4], 10], "non-existent item")
test_function(3, [[1, 2, 3, 4, 5, 6, 7], 3], "non-rotated array")
test_function(4, [[6, 7, 8, 9, 10, 1, 2, 3, 4], 6], "front of rotation")
test_function(5, [[6, 7, 8, 9, 10, 1, 2, 3, 4], 3], "back of rotation")
test_function(6, [[6, 7, 8, 1, 2, 3, 4], 8], "highest item in array")
test_function(7, [[6, 7, 8, 1, 2, 3, 4], 1], "lowest item in array")