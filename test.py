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

def TopK2(nums: list, k: int) -> int:
#    方法2、快排