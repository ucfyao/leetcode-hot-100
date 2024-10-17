#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.07%)
# Likes:    2505
# Dislikes: 0
# Total Accepted:    560K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#
# import collections
# from typing import List

# 理解的不是很好，需要复习。
# 为什么 count 可以累积。

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 要求的连续子数组
        count = 0
        n = len(nums)
        preSums = collections.defaultdict(int)
        preSums[0] = 1
        # print(f'init preSums: {preSums}')

        presum = 0
        for i in range(n):
            # print(f'=======Index: {i}========')
            # print(f'Current Num: {nums[i]}')

            # 数组 nums 中从第一个元素到索引 i 的和
            presum += nums[i]

            # print(f'presum: {presum}')
            # print(f'k: {k}')
            # print(f'presum-k: {presum - k}')
            # print(f'preSums[presum-k]: {preSums[presum - k]}')

            # 如果 presum - k 有值，代表该该前缀和出现在 i 之前的某个位置。且这个位置到 i 的子数组和为 k。
            # 利用 defaultdict 的特性，当 presum-k 不存在时，返回的是 0。这样避免了判断。
            # defaultdict(int) 中，int 的默认值是 0，当键不存在时，defaultdict 会自动插入该键并将其值设为 0。
            count += preSums[presum - k]

            # 打印更新后的count值
            # print(f'Updated Count: {count}')

            # 给前缀和为 presum 的个数加 1
            # 每次把前缀和放到列表中
            preSums[presum] += 1

            # 打印 preSums 的更新
            # print(f'Updated PreSums[Presum]: {preSums}')

        return count


# # 测试调用方法
# solution = Solution()  # 创建Solution类的实例
# nums = [1, 1, 0, 2, 4, -1, 1, 13, -1, 1, 1]  # 输入数组
# k = 2  # 目标和
# result = solution.subarraySum(nums, k)  # 调用方法
# print(result)  # 输出结果

# @lc code=end

