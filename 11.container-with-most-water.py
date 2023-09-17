#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (54.14%)
# Likes:    26598
# Dislikes: 1455
# Total Accepted:    2.4M
# Total Submissions: 4.4M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
#
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
#
# Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
#
# Constraints:
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#
        # for i, h1 in enumerate(height):
        #     for j, h2 in enumerate(height):
        #         water = abs(i - j) * min(h1,h2)
        #         if (water > maxWater):
        #             maxWater = water
# @lc code=start
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height) - 1

        while left < right:
            water = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, water)

            if height[left] < height[right]:
                old_height = height[left]
                while left < right and height[left] <= old_height:
                    left += 1
            else:
                old_height = height[right]
                while right > left and height[right] <= old_height:
                    right -= 1

        return maxWater

# testcase = [2,3,4,5,18,17,6]
# print(Solution().maxArea(testcase))
# @lc code=end


            # if (height[left + leftiter] == height[right + rightIter]):
            #     if (leftiter < abs(rightIter)):
            #         left += leftiter
            #     elif (leftiter < abs(rightIter)):
            #         right += rightIter
            #     elif (height[left] < height[right]):
            #         left += leftiter
            #     else:
            #         right += rightIter

            # elif (height[left + leftiter] > height[right + rightIter]):
            #     left += leftiter
            # else:
            #     right += rightIter