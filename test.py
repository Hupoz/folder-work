# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:20:48 2020

@author: win10
"""
def TopK1(nums: list, k: int) -> int:
#    方法1、排序，输出第K大的数；排序的最优时间复杂度为NlogN，快排或者sort（）函数，Timsort（）
    if not nums or k > len(nums):
        return
    nums.sort()
    return nums[-k]

#a = [1,2,3,4,5]
#k = 5
#res = TopK1(a, k)
#print(res)
class Solution1:
    # 方法2、取中间索引值，修改数组令左边均大于索引值,右边均小于，
    # 再判断索引与k-1的大小，选择左或右子列表
    # 时间复杂度为N
    def partition(self, nums):
        r, l = 0, len(nums) - 1
        index = (r + l)// 2
        left_list = [x for x in nums if x >= nums[index]]
        right_list = [x for x in nums if x < nums[index]]
        nums = left_list + right_list
        return len(left_list) - 1
    
    def TopK2(self, nums: list, k: int) -> int:
        if not nums or k > len(nums):
            return
        index = self.partition(nums)
        while index != k - 1:
            if index > k - 1:
                nums = nums[:index - 1]
                index = self.partition(nums)
            else:
                nums = nums[index + 1:]
                index = self.partition(nums)
        return nums[index]

# =====================================
def Cal(s: str)-> float:
    return eval(s)  # 方法1、eval（）函数

# s = input('请输入计算式：')
# Cal(s)

# =====================================
def printContent(s: str):
    import os
    for dirpath, dirnames, filenames in os.walk(s):  # os.walk()-遍历目录的所有子文件和子文件夹
        print('该层路径为：', dirpath)
        if dirnames:
            print('文件夹名称：', dirnames)
        else:
            print('无文件夹')
        if filenames:
            print('文件名称：', filenames)
        else:
            print('无文件')

# printContent(r'D:\test')
# =====================================
    