#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.65%)
# Likes:    17799
# Dislikes: 784
# Total Accepted:    1.3M
# Total Submissions: 2.7M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
# [100,4,200,1,3,2]
#
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)

        num_set = set(nums)

        curr_count = 1
        max = 0
        for i in nums:
            right = i
            left = i
            while right+1 in num_set:
                curr_count += 1
                if right in num_set:
                    num_set.remove(right)
                right += 1
            while left-1 in num_set:
                curr_count += 1
                if left in num_set:
                    num_set.remove(left)
                left -= 1

            if curr_count > max:
                max = curr_count
            curr_count = 1

        return max
# @lc code=end

