#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode.cn/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (75.45%)
# Likes:    1881
# Dislikes: 0
# Total Accepted:    543.8K
# Total Submissions: 710.4K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
#
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
#
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#
#
# 示例 2:
#
#
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
#
#
#
#
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）
#
#

# @lc code=start
# 解法1：前缀后缀积
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         answer = [0] * n

#         # 1. 先计算左边的乘积
#         # 第一位右边没有数据，初始化为1
#         answer[0] = 1
#         for i in range(1, n):
#             answer[i] = nums[i-1] * answer[i-1]

#         # 2. 计算右边乘积
#         R = 1
#         for i in reversed(range(n)):
#             answer[i] = answer[i] * R
#             R *= nums[i]

#         return answer

# 解法2：一次遍历出结果

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ra = [1] * n  # 初始化结果数组为1

        pre = 1  # 前缀乘积初始化为1
        suf = 1  # 后缀乘积初始化为1

        for i in range(1, n):
            pre *= nums[i - 1]  # 计算前缀乘积
            suf *= nums[n - i]  # 计算后缀乘积
            ra[i] *= pre  # 更新结果数组，乘上前缀乘积
            ra[n - i - 1] *= suf  # 更新结果数组，乘上后缀乘积

        return ra  # 返回结果数组

# @lc code=end

