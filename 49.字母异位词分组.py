#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# 定义字典

# list：传递给 defaultdict 的参数，用于指定字典的默认值类型。在这个例子中，每当访问一个不存在的键时，defaultdict 将自动为该键创建一个新的空列表作为其值。
#
# sort与sorted
# sort 是列表（list）对象的一个方法，用于对列表进行原地排序，这意味着它直接修改原列表，而不返回任何值（实际上返回 None）。
# sorted 是Python的内置函数，可以对任何可迭代的对象进行排序，包括但不限于列表、元组、字典和字符串，返回一个新的排序列表，原始数据不会被修改。


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 定义字典
        # collections.defaultdict 是 Python 标准库 collections 模块中的一种数据结构，它是字典（dict）的一个子类。它的特点是在访问不存在的键时，能自动创建一个默认值，避免了直接使用普通字典时可能遇到的 KeyError。
        # list：传递给 defaultdict 的参数，用于指定字典的默认值类型。在这个例子中，每当访问一个不存在的键时，defaultdict 将自动为该键创建一个新的空列表作为其值。
        mp = collections.defaultdict(list)
        for st in strs:
            # sort与sorted
            # sort 是列表（list）对象的一个方法，用于对列表进行原地排序，这意味着它直接修改原列表，而不返回任何值（实际上返回 None）。
            # sorted 是Python的内置函数，可以对任何可迭代的对象进行排序，包括但不限于列表、元组、字典和字符串，返回一个新的排序列表，原始数据不会被修改。

            # join方法
            # join 是字符串类型的一个方法，用于将序列中的元素连接成一个新的字符串。
            # '连接符'.join(序列)
            # 这里的 '连接符' 是希望在序列元素之间插入的字符串，而 序列 是一个包含多个字符串的可迭代对象，如列表、元组或字符串集合。

            key = "".join(sorted(st))

            # 这里append方法的使用
            # 在 Python 中，字典类型本身没有 append 方法。append 方法是列表（list）的一个方法，用于向列表末尾添加一个元素。
            # map["new_key"].append("new_value") 这里的 append 方法实际上是作用于字典 map 中键 "new_key" 对应的值上，而不是直接作用于字典本身。
            # 它的意思是：“在字典 map 中，将 "new_value" 添加到键 "new_key" 对应的列表中。” 如果 "new_key" 还没有对应的值，则首先创建一个空列表，然后再执行添加操作。
            mp[key].append(st)
        return list(mp.values())
# @lc code=end

