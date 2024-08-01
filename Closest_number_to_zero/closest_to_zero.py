"""
Find Closest Number to Zero

Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

"""

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        possible_value = 10**6

        neg_possible_value = -possible_value

        for x in nums:

            if x < possible_value and neg_possible_value <= x:
                if x < 0:
                    neg_possible_value = x
                else:
                    possible_value = x
        
        if possible_value <= -neg_possible_value:
            return possible_value
        else:
            return neg_possible_value
        