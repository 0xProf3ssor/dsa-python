"""
Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

Examples:

Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1
Explanation: Since, 1 is present more than 7/2 times, so it is the majority element.
Input: arr[] = [7]
Output: 7
Explanation: Since, 7 is single element and present more than 1/2 times, so it is the majority element.
Input: arr[] = [2, 13]
Output: -1
Explanation: Since, no element is present more than 2/2 times, so there is no majority element.
"""


class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        count = 0
        candidate = None

        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Verify if the candidate is indeed the majority element
        if arr.count(candidate) > n // 2:
            return candidate
        else:
            return -1


def test_case_1():
    arr = [1, 1, 2, 1, 3, 5, 1]
    expected = 1
    assert Solution().majorityElement(arr) == expected


def test_case_2():
    arr = [7]
    expected = 7
    assert Solution().majorityElement(arr) == expected


def test_case_3():
    arr = [2, 13]
    expected = -1
    assert Solution().majorityElement(arr) == expected
