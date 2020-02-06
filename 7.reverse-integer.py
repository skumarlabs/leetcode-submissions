#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.62%)
# Likes:    2801
# Dislikes: 4397
# Total Accepted:    936.7K
# Total Submissions: 3.7M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num_str = str(x)[1:]
            num_len = len(num_str)-1
            num = int("-"+"".join([num_str[i] for i in range(num_len, -1, -1)]))
        else:
            num_str = str(x)
            num_len = len(num_str)-1
            num = int("".join([num_str[i] for i in range(num_len, -1, -1)]))
        if num < (-2**31) or num >= 2**31:
            return 0
        else:
            return num
# @lc code=end

