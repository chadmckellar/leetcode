#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (45.30%)
# Likes:    7849
# Dislikes: 7683
# Total Accepted:    2.2M
# Total Submissions: 4.8M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) in [0,1]:
            return True

        new_s = ''.join(c for c in s if c.isalnum())
        new_s_length = len(new_s)
        center = (len(new_s)//2)
        left = 0
        right = new_s_length - 1

        while left != center:
            if new_s[left].lower() != new_s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

x = Solution()
x.isPalindrome("A man, a plan, a canal: Panama")
# @lc code=end

