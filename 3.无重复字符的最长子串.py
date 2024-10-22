#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (39.72%)
# Likes:    10383
# Dislikes: 0
# Total Accepted:    3.1M
# Total Submissions: 7.7M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
#
#
#
# 示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 解法1： 这个题明显用窗口滑动比较简单。第一次碰到String相关的问题，请记得String存储结构为数组。
        # 首先初始化一个哈希表记录窗口
        dic = {}

        # 定义左指针
        left = 0

        # 初始化窗口长度
        res = 0

        # 循环全部字符串
        for i in range(len(s)):
            # 如果字符在窗口中出现过，那么移动左侧指针为出现位置的后一位。
            if s[i] in dic:
                left = dic[s[i]] + 1

            # 计算窗口长度，当前位置减去左指针的位置 + 1
            res = max(res, i - left + 1)

            # 将字符存储在字典中
            dic[s[i]] = i

        return res




# @lc code=end

