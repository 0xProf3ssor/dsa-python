"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

"""
To Solve the problem, we can use a hash map to store the indices of the numbers we have seen so far.
We can iterate through the array and for each number, we can check if the complement (target - number) exists in the hash map.
If it does, we return the indices of the current number and the complement. If it doesn't, we add the current number and its index to the hash map.
"""

from loguru import logger


class Solution(object):
    def twoSum(self, nums, target):
        map = {}

        for i, num in enumerate(nums):
            r = target - num
            if r in map:
                return [i, map[r]]
            map[num] = i


solution = Solution()


def test_case_1():
    logger.info("Running test case 1")
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 0], (
        f"Expected [0, 1] but got {solution.twoSum([2, 7, 11, 15], 9)}"
    )
    logger.success("Test case 1 passed")


def test_case_2():
    logger.info("Running test case 2")
    assert solution.twoSum([3, 2, 4], 6) == [2, 1], (
        f"Expected [1, 2] but got {solution.twoSum([3, 2, 4], 6)}"
    )
    logger.success("Test case 2 passed")


def test_case_3():
    logger.info("Running test case 3")
    assert solution.twoSum([3, 3], 6) == [1, 0], (
        f"Expected [0, 1] but got {solution.twoSum([3, 3], 6)}"
    )
    logger.success("Test case 3 passed")
