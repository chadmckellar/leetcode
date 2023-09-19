#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (59.86%)
# Likes:    29071
# Dislikes: 414
# Total Accepted:    1.7M
# Total Submissions: 2.8M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_container_height = 0
        total_container_size = 0
        left_last_adjusted = None
        while left < right:
            if (total_container_size > 0):
                if (left_last_adjusted == True):
                    if (height[left] > 0):
                        total_container_size -= min(max_container_height, height[left])
                else:
                    if (height[right] > 0):
                        total_container_size -= min(max_container_height, height[right])

            inner_container_height = min(height[left], height[right])
            if (inner_container_height > max_container_height):
                container_height_delta = inner_container_height - max_container_height
                max_container_height = inner_container_height
                total_container_size += container_height_delta * (right - left - 1)

            if (height[left] < height[right]):
                left += 1
                left_last_adjusted = True
            else:
                right -= 1
                left_last_adjusted = False

        return total_container_size

test_case = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(test_case))
# @lc code=end

