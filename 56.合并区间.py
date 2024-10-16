#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (49.92%)
# Likes:    2436
# Dislikes: 0
# Total Accepted:    982.2K
# Total Submissions: 1.9M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例 1：
#
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2：
#
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
# 提示：
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#

# @lc code=start
# 解法1：合并区间

# （1）思路解释
# 这道题要求将一系列可能重叠的区间进行合并。要实现这个，我们需要先将所有区间按照起始值排序，这样我们可以从头开始遍历，逐个判断每个区间是否和前面的区间有重叠（即当前区间的起点是否小于等于前一个区间的终点）。如果重叠，我们更新终点，否则，将当前合并的区间存入结果列表，并开始处理新的区间。

# （2）步骤
# 排序：首先按区间的起始值进行排序，以保证遍历时可以从小到大处理区间。
# 初始化：将第一个区间作为当前正在处理的区间的起始值和终止值。
# 遍历区间：从第二个区间开始，判断当前区间的起点是否大于上一个区间的终点：
# 如果不重叠：将前一个区间加入结果列表，并更新当前区间的起始值和终点值。
# 如果重叠：更新终点为当前区间和前一个区间终点的较大值。
# 最后处理：遍历结束后，将最后的合并区间加入结果列表。
# 返回结果：输出合并后的区间。

# （3）复杂度
# 时间复杂度：排序的时间复杂度为 O(n log n)，其中 n 是区间的数量。遍历所有区间的时间复杂度为 O(n)。因此，总的时间复杂度为 O(n log n)。
# 空间复杂度：除了结果列表外，算法只需要常数级别的额外空间，因此空间复杂度为 O(n)。
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 对区间按起始值进行排序
        intervals.sort(key=lambda x: x[0])

        # 用于存储结果的列表
        res = []

        # 初始化：取第一个区间的起点和终点作为初始值
        start, end = intervals[0]

        # 遍历剩下的区间
        for left, right in intervals[1:]:
            # 如果当前区间与前一个区间不重叠
            if left > end:
                # 将前一个合并区间加入结果列表
                res.append([start, end])
                # 更新起点和终点为当前区间
                start = left
                end = right
            else:
                # 如果区间重叠，更新终点为两个区间的较大值
                end = max(end, right)

        # 将最后一个区间加入结果列表
        res.append([start, end])

        # 返回合并后的区间
        return res
# @lc code=end

