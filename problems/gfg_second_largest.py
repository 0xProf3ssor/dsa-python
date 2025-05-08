def second_largest(arr):
    """
    Function to find the second largest element in an array.
    :param arr: List of integers
    :return: Second largest integer in the array or -1 if not found
    """
    arr = sorted(arr)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] != arr[-1]:
            return arr[i]
    return -1


def test_case_1():
    assert second_largest([1, 2, 3, 4, 5]) == 4


def test_case_2():
    assert second_largest([5, 5, 5, 5]) == -1


def test_case_3():
    assert second_largest([10, 20, 20, 30]) == 20


def test_case_4():
    assert second_largest([1]) == -1
