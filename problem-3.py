def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return []
    quicksort(input_list)
    numbers = [0,0]
    for index, number in enumerate(input_list):
        numbers_index = index % 2
        numbers[numbers_index] += get_number(number, (index // 2))
    return numbers
    pass

def quicksort(input_list):
    quicksort_helper(input_list, 0, len(input_list) - 1)

def quicksort_helper(input_list, start, end):
    if end <= start:
        return
    pivot_index = sort_pivot(input_list, start, end)
    quicksort_helper(input_list, start, pivot_index - 1)
    quicksort_helper(input_list, pivot_index + 1, end)

def sort_pivot(input_list, start, end):
    pivot_index = end
    left_index = 0

    pivot = input_list[pivot_index]

    while left_index != pivot_index:
        if input_list[left_index] <= pivot:
            left_index += 1
            continue

        input_list[pivot_index] = input_list[left_index]
        input_list[left_index] = input_list[pivot_index - 1]
        input_list[pivot_index - 1] = pivot
        pivot_index -= 1
    return pivot_index


def get_number(number, ten_power):
    result = number
    while ten_power:
        result *= 10
        ten_power -= 1
    return result

def test_function(test_number, test_case, test_subject):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    result = None
    if sum(output) == sum(solution):
        result = "Pass"
    else:
        result = "Fail"
    print("{} - {} - {} - {}".format(test_number, result, test_subject,  output))


test_function(1, [[], [0, 0]],  "empty array") # []
test_function(2, [[3, 3, 3, 3, 3], [333, 33]], "same number") # [333, 33]
test_function(3, [[1, 2, 3, 4, 5], [542, 31]], "normal use case") # [531, 42]
test_function(4, [[4, 6, 2, 5, 9, 8], [964, 852]], "normal use case") # [852, 964]
