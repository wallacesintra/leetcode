/*
Given an integer array nums of length n, 
you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    var nums2 = nums;
    var n = nums.length;
    
    for (var i = 0; i < n; i++){
        nums.push(nums2[i]);
    } 
    return nums;
};