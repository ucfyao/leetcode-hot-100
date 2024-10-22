#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 记录最长连续序列
        res = 0

        # 将 nums 转为集合，使用集合的目的
        # 1. 去重，将列表 nums 转换成一个集合 set，自动移除所有重复的元素。集合是一种不允许重复元素的数据结构，因此任何加入集合中的重复元素都会被自动忽略。
        # 2. 是为了快速检查某个元素是否存在，因为集合（Set）在 Python 中是基于哈希表实现的，这意味着它可以在平均时间复杂度为 O(1) 的条件下完成元素的查找、添加和删除操作。
        num_set = set(nums)

        for num in num_set:
            # 检查 num - 1 是否不在集合中。这一步是为了确定 num 是否是某个连续序列的起点。如果 num - 1 在集合中，则 num 不是起点，因为存在比它小的连续数字。
            if (num - 1) not in num_set:
                # 如果 num 是连续序列的起点，则初始化连续序列长度 cont 为 1。
                cont = 1
                current_num = num
                #  使用一个循环来查找以 num 开始的连续序列。只要 num + 1 在集合中，就持续更新 num 为 num + 1 并增加 cont。
                while (current_num + 1) in num_set:
                    # 每找到一个连续的元素，就将序列长度增加 1。
                    cont += 1
                    # 更新 current_num 为下一个连续的数字，继续检查是否存在。
                    current_num += 1
                # 每次循环结束后，比较并更新记录的最长连续序列长度 res。
                res = max(res, cont)
        return res
# @lc code=end

