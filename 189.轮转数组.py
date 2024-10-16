#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
# https://leetcode.cn/problems/rotate-array/description/
#
# algorithms
# Medium (44.85%)
# Likes:    2259
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
#
#
#
# 进阶：
#
#
# 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#
#
#

# @lc code=start
# 解法1：极简Python风

# 1）思路解释：
# 利用Python的切片特性和取模运算，将数组按照旋转的步数分割成两部分，然后将这两部分拼接在一起，完成数组的原地旋转。通过取模操作避免不必要的多余旋转。

# （2）步骤：
# 使用 k %= len(nums) 来计算实际需要旋转的步数，确保旋转次数不超过数组长度。
# 通过切片 nums[-k:] 获取数组的最后 k 个元素，这将是旋转后的前部分。
# 使用 nums[:-k] 获取剩余部分，这将成为旋转后的后部分。
# 利用 nums[:] = nums[-k:] + nums[:-k] 直接修改原数组为旋转后的结果。

# （3）复杂度：
# 时间复杂度：O(n)，因为切片和拼接操作都需要遍历整个数组。
# 空间复杂度：O(n)，由于切片操作创建了新数组（尽管最终覆盖原数组）。

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 计算有效的旋转步数，避免多余的旋转
        k %= len(nums)

        # 使用切片重新排列数组
        # nums[-k:] 是最后 k 个元素
        # nums[:-k] 是前 len(nums) - k 个元素
        # nums[:] 确保修改的是原数组。如果你使用 nums = ...，它会将 nums 指向一个新的列表对象，而不修改原数组的内容。
        nums[:] = nums[-k:] + nums[:-k]


# @lc code=end

