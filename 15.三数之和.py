#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (37.88%)
# Likes:    7101
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 5.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#
# 示例 3：
#
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 长度
        n=len(nums)
        if(not nums or n<3):
            return []
        # 排序
        nums.sort()
        # 初始化返回
        res=[]

        for i in range(n):
            # 因为已经从小到大排序，假如当前值大于0之后，在之后的组合，都是正数，正数相加永远大于0，所以直接退出。
            if(nums[i] > 0):
                return res
            # 如果当前数和上一个相同，那么无需本次循环
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            # 指针初始化
            L = i + 1
            R = n - 1

            # 循环找相加为0的组合
            while(L < R):
                if(nums[i] + nums[L] + nums[R] == 0):
                    # 如果找到组合，将组合加入返回值中
                    res.append([nums[i],nums[L],nums[R]])

                    # 快速移动过滤重复数据
                    while(L < R and nums[L] == nums[L+1]):
                        L = L+1
                    while(L < R and nums[R] == nums[R-1]):
                        R = R-1
                    # 指针移动
                    L = L+1
                    R = R-1
                # 如果相加大于0，说明右侧大了，那么移动右侧指针
                elif(nums[i] + nums[L] + nums[R] > 0):
                    R = R-1
                # 相反如果3个数相加小于0，说明左侧太小了，那么移动左侧指针
                else:
                    L = L+1
        return res

# @lc code=end

