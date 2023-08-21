#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.38%)
# Likes:    15631
# Dislikes: 549
# Total Accepted:    1.6M
# Total Submissions: 2.6M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for x in range(0, len(nums))]
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for c in count:
            freq[count.get(c) - 1].append(c)

        result = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                result.append(j)
                if (len(result)) == k:
                    return result

# @lc code=end

