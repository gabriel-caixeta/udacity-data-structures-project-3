def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_next_index = 0
    two_start_index = len(input_list) - 1
    current_index = 0

    while current_index <= two_start_index:
        item = input_list[current_index]
        if item == 0:
            input_list[current_index] = input_list[zero_next_index]
            input_list[zero_next_index] = item
            zero_next_index += 1        
            current_index += 1
        elif item == 1:
            current_index += 1
        elif item == 2:
            input_list[current_index] = input_list[two_start_index]
            input_list[two_start_index] = item
            two_start_index -= 1
        else:
            return None
    return input_list
    
def test_function(test_number, test_case, test_description):
    allowed_numbers = [0,1,2]
    sorted_array = sort_012(test_case)
    correct_array = sorted(test_case)
    result = ""
    if sorted_array == sorted(test_case):
        result = "Pass"
    else:
        if correct_array[0] not in allowed_numbers or correct_array[-1] not in allowed_numbers:
            if sorted_array == None:
                result = "Pass"
            else:
                result = "Fail"
            return
        result = "Fail"
    print("{} - {} - {}".format(test_number, result, test_description))

test_function(1, [], "empty array")
test_function(2, [1], "single item in array")
test_function(3, [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], "sorted array")
test_function(4, [1,2,0,0,1,2,0,3,2,1], "unknown number")
test_function(5, [1,2,2,1,1,2,1,2,1,2,2,1,1,1,2,1], "missing one of the numbers")
test_function(6, [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1], "normal usecase")
