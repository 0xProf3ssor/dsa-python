"""
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order).

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.
"""

"""
To solve the problem of finding the next permutation of an array of integers, we can follow these steps:
1. Traverse the array from right to left and find the first pair of adjacent elements (arr[i], arr[i+1]) such that arr[i] < arr[i+1]. This identifies the rightmost ascent in the array.
2. If no such pair is found, it means the array is in descending order, and we can simply reverse the entire array to get the smallest permutation.
3. If such a pair is found, we need to find the smallest element in the right subarray (arr[i+1] to arr[n-1]) that is greater than arr[i]. Let's call this element arr[j].
4. Swap arr[i] and arr[j].
5. Reverse the right subarray (arr[i+1] to arr[n-1]) to get the next permutation.
"""

from typing import List


def next_permutation(arr):
    n = len(arr)

    # Find the first index `i` from the end where arr[i] < arr[i + 1]
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        # Find the first index `j` from the end where arr[j] > arr[i]
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]

    # Reverse the subarray from i+1 to the end
    arr[i + 1 :] = reversed(arr[i + 1 :])

    return arr


# Tests
def test_case_1():
    assert next_permutation([1, 2, 3]) == [1, 3, 2], (
        f"expected [1, 3, 2] but got {next_permutation([1, 2, 3])}"
    )


def test_case_2():
    assert next_permutation([3, 2, 1]) == [1, 2, 3]


def test_case_3():
    assert next_permutation([1, 1, 5]) == [1, 5, 1]


def test_case_4():
    assert next_permutation([1]) == [1]


def test_case_5():
    assert next_permutation([1, 2]) == [2, 1]


def test_case_6():
    assert next_permutation([2, 4, 1, 7, 5, 0]) == [2, 4, 5, 0, 1, 7]


def test_case_7():
    assert next_permutation([3, 4, 2, 5, 1]) == [3, 4, 5, 1, 2]
