#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 官方解法：双指针采用快速排序的思路
        # n = len(nums)

        # left = right = 0
        # while right < n:
        #     if nums[right] != 0:
        #         # 当 nums[right] 不为0时，将其值与 nums[left] 交换。
        #         # 可以优化：即便 left 和 right 指向相同的元素，也会执行交换（实际上这不会改变数组，但仍然会进行操作）。
        #         nums[left], nums[right] = nums[right], nums[left];
        #         left += 1;
        #     right += 1;

        # 解法 2 思路：用指针保存相对位置，然后覆盖值，最后将剩余的位置补0。
        # 初始化插入位置，指示下一个非零元素应插入的位置
        insert_pos = 0

        # 第一次遍历数组，将所有非零元素移动到数组的前面
        for num in nums:
            if num != 0:
                # 如果当前元素不是零，将其放在insert_pos指示的位置
                nums[insert_pos] = num
                insert_pos += 1  # 插入位置向后移动

        # 第二次遍历，将剩余的位置用零填充
        while insert_pos < len(nums):
            nums[insert_pos] = 0  # 将当前位置赋值为0
            insert_pos += 1  # 插入位置继续向后移动，直到数组末尾

# @lc code=end


