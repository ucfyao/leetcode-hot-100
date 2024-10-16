#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# https://leetcode.cn/problems/maximum-subarray/description/
#
# algorithms
# Medium (55.28%)
# Likes:    6807
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 3.4M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
# 示例 2：
#
#
# 输入：nums = [1]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#
#

# @lc code=start
# 解法1：暴力解一切。(可惜，能解但是超时了。)
# （1）暴力解法的核心思想是通过穷举所有可能的子数组，然后计算每个子数组的和，最后取其中的最大值。
# 这种方法相对直观，大家如果没有好的思路都可以尝试用暴力解法。
# 但它的时间复杂度较高为 O(n²) 或 O(n³)，在处理较大数组时效率较低。
#
# （2）暴力解法的步骤：
# 遍历数组中的所有可能的子数组（通过两重或三重循环）。
# 对于每个子数组，计算它的和。
# 记录当前的最大子数组和，最后返回这个值。

# （3）时间复杂度
# 时间复杂度O(n²)
# 空间复杂度O(1)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # 初始化为负无穷，表示最小的可能值
#         max_sum = -float('inf')

#         # 遍历所有可能的子数组
#         for i in range(len(nums)):  # 外层循环：确定子数组的起始位置
#             current_sum = 0  # 用于累加从 i 开始的子数组的和
#             for j in range(i, len(nums)):  # 内层循环：确定子数组的结束位置
#                 current_sum += nums[j]  # 累加当前元素
#                 if current_sum > max_sum:
#                     max_sum = current_sum  # 更新最大和

#         return max_sum


# 解法2：超强动态规划（完美通过）
# （1）动态规划解法，称为 Kadane's Algorithm（卡丹算法），用于解决最大子数组和问题（Maximum Subarray Problem）。该算法的目标是找到一个数组中和最大的连续子数组，并且时间复杂度为 O(n)，非常高效。
# Kadane's Algorithm 的核心思想：
# 贪心策略：如果当前的子数组和变成负数或者小于当前元素，那么继续累加这些负值只会让结果变得更差。此时就可以抛弃之前的子数组，从当前元素重新开始新的子数组。
# 动态规划：对于数组中的每个元素，算法计算该元素要么加入之前的子数组，要么从当前元素开始重新计算子数组的和。通过取这两者的最大值来更新当前的子数组和。
# 最优解：在遍历数组时，记录当前为止的最大子数组和，并逐步更新这个值，最终返回的就是最大子数组和。
#
# （2）Kadane's Algorithm 的步骤：
# 初始化两个变量：current_sum（当前子数组和）和 max_sum（全局最大子数组和）。初始值都为数组的第一个元素。
# 遍历数组，对于每个元素：
# 计算当前子数组和 current_sum = max(num, current_sum + num)，决定是将当前元素加入子数组还是从当前元素重新开始子数组。
# 更新最大子数组和 max_sum = max(max_sum, current_sum)。
# 遍历完数组后，max_sum 就是最大子数组和。
#
# （3）算法的时间复杂度和空间复杂度：
# 时间复杂度: O(n)，因为只需要遍历数组一次。
# 空间复杂度: O(1)，因为只需要常数空间存储 current_sum 和 max_sum。
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         current_sum = max_sum = nums[0]
#         for num in nums[1:]:
#             # 如果当前子数组的和小于0，则重新开始子数组
#             current_sum = max(num, current_sum + num)
#             # 更新最大子数组的和
#             max_sum = max(max_sum, current_sum)

#         return max_sum

# 动态规划 + 贪心策略：
# （1）在每一步，比较当前元素 nums[i] 和 current_sum + nums[i]。这决定了是将当前元素加入现有子数组，还是从当前元素开始一个新的子数组。通过取两者的最大值，确保我们选的是更优的子数组方案。

# （2）最优解更新：
# 每次更新 current_sum 后，比较 max_sum 和 current_sum，确保 max_sum 保存全局最大子数组的和。

# （3）复杂度：
# 时间复杂度：O(n)，因为只需要遍历数组一次。
# 空间复杂度：O(1)，只使用了常数的额外空间用于存储 max_sum 和 current_sum。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化为负无穷，表示最小的可能值
        max_sum = -float('inf')
        # 存储当前最大值
        current_sum = 0

        # 遍历所有可能的子数组
        for i in range(len(nums)):
            # 累加当前连续数组
            current_sum += nums[i]
            # 如果当前连续子数组的最大值大于记录的最大值，更新最大值
            if current_sum > max_sum:
                # 更新最大值
                max_sum = current_sum
            # 如果当前连续子数组的最大值为负数，将 current_sum 置为0，因为负数 + 随便一个值，都小于这个值。
            if(current_sum < 0):
                current_sum = 0
        return max_sum

# @lc code=end

