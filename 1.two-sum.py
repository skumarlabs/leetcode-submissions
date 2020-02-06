#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_length = len(nums)
        for i, n in enumerate(nums):
            temp_num = target - n
            j = i+1
            while(j < num_length):
                if nums[j] == temp_num:
                    return [i, j]
                j += 1


        
# @lc code=end

