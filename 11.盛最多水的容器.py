#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode.cn/problems/container-with-most-water/description/
#
# algorithms
# Medium (60.10%)
# Likes:    4955
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 2.1M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。
#
#
#
# 示例 1：
#
#
#
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
# 示例 2：
#
#
# 输入：height = [1,1]
# 输出：1
#
#
#
#
# 提示：
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
# 解法1： 暴力破解
        # 时间复杂度：O(N^2)，每对线段都需要比较一次
        # 空间复杂度：O(1)，只需要额外的常数级别的空间
        # n = len(height)
        # max_area = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         area = min(height[i], height[j]) * (j - i)
        #         max_area = max(max_area, area)

        # 解法2： 双指针
        # 时间复杂度：O(N)，双指针总计最多遍历整个数组一次
        # 空间复杂度：O(1)，只需要额外的常数级别的空间
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
# @lc code=end