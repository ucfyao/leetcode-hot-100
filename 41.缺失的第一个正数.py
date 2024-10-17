#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (44.45%)
# Likes:    2217
# Dislikes: 0
# Total Accepted:    449.5K
# Total Submissions: 983.3K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。
#
# 示例 2：
#
#
# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。
#
# 示例 3：
#
#
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc code=start
# 解法1：哈希大法
# 万能解法除了暴力解就是哈希解了。

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         # 1. 将全部的 < 0 和大于 N 的置为0
#         for i in range(n):
#             if nums[i] < 0 or  nums[i] > n:
#                 nums[i] = 0

#         # 2. 将数值放到对应的哈希
#         for j in range(n):
#             while 1 <= nums[j] <= n and nums[nums[j] - 1] != nums[j]:
#                 nums[nums[j] - 1], nums[j] = nums[j], nums[nums[j] - 1]

#         # 3. 查看是否有为0的
#         for i in range(n):
#             if nums[i] != i+1:
#                 return i + 1
#         return n + 1

# 解法2 ：哈希大法2
# 通过偏移，减少循环次数。

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 取值范围是：[1,n+1]，所以哈希长度为 n+1
        hash_size = n + 1

        # 1. 将全部的 < 0 和大于 N 的置为0
        for i in range(n):
            if nums[i] < 0 or  nums[i] > n:
                nums[i] = 0

        # 2. 将数值放到对应的哈希
        for i in range(n):
            # 假设数组的任意元素都应该是 nums[i] % hash_size == nums[i]
            # 取余为 0：判断 nums[i] 是否是 hash_size 的倍数
            if nums[i] % hash_size != 0:
                # 计算哈希位置 pos，nums[i] 对 hash_size 取余后，减 1 得到新的索引位置
                pos = (nums[i] % hash_size) - 1

                # 如果数字 x 出现，则给 nums[x−1] 加上 hash_size
                # 先取余再加：这相当于给现有的值增加一个偏移量，防止与原有数值冲突。
                nums[pos] = (nums[pos] % hash_size) + hash_size

        # 3. 遍历数组
        for i in range(n):
            # 若 nums[i] < hash_size, 则说明 i+1 没有出现，返回 i+1
            if nums[i] < hash_size:
                return i + 1
        return hash_size

# @lc code=end

