#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (63.45%)
# Likes:    5352
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # # 解法1：双指针最容易理解，也是高效的解决方案
        # # 时间复杂度：O(n)，因为每个柱子只会被访问一次。
        # # 空间复杂度：O(1)，只用了固定的额外空间来存储指针和最大高度。

        # n = len(height)

        # # 初始化左右指针，left 指向最左边，right 指向最右边
        # left = 0
        # right = n - 1

        # # 初始化左右两边的最大高度，分别从两端柱子开始。
        # # 这两个值决定了当前指针所能存储的雨水量。
        # left_max = height[left]
        # right_max = height[right]

        # # 初始化累计的雨水量为0
        # res = 0

        # # 当左指针小于右指针时，继续遍历整个数组
        # # 指针逐步向中间移动，每次移动都计算当前能接的雨水量
        # while left < right:
        #     # 如果左边的柱子较低，那么左边可以存水，向右移动左指针
        #     if left_max < right_max:
        #         left += 1
        #         # 更新左侧的最大高度
        #         left_max = max(left_max, height[left])

        #         # 当前可以存的雨水量为 left_max 减去当前柱子的高度
        #         # 如果当前柱子低于 left_max，则可以存储一些水
        #         res += left_max - height[left]
        #     else:
        #         # 如果右边的柱子较低，那么右边可以存水，向左移动右指针
        #         right -= 1
        #         # 更新右侧的最大高度
        #         right_max = max(right_max, height[right])

        #         # 当前可以存的雨水量为 right_max 减去当前柱子的高度
        #         # 如果当前柱子低于 right_max，则可以存储一些水
        #         res += right_max - height[right]

        # # 返回累计的雨水量
        # return res

        # 解法2：动态规划，for有点多
        if not height:
            return 0

        n = len(height)
        # 初始化两个数组，分别存储每个位置左侧和右侧的最大高度
        left_max = [0] * n
        right_max = [0] * n

        # 计算每个位置左侧的最大高度
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # 计算每个位置右侧的最大高度
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # 计算每个位置能够存储的雨水量
        res = 0
        for i in range(n):
            # 如果左右两侧的最大高度都比当前高度大，说明该位置能够存储雨水，否则存储量为零。
            # 当前位置左右两侧最大高度的较小值减去当前柱子的高度。
            # 也就是每个位置存储的水量为 min(left_max[i], right_max[i]) - height[i]
            res += min(left_max[i], right_max[i]) - height[i]

        return res

# @lc code=end

