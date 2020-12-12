#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:hello_life 
@license: Apache Licence 
@file: 02_数据流中的中位数.py 
@time: 2020/12/12
@software: PyCharm 
description:如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
"""
import heapq
class MedianFinder:
    def __init__(self):
        """
        定义一个小顶推，一个大顶堆
        小顶堆存储大数，大顶堆存储小数
        如果长度为奇数，小顶堆的元素比大顶推元素多一
        initialize your data structure here.
        """
        self.min_stack=[]
        self.max_stack=[]

    def addNum(self, num: int) -> None:
        #极小堆中数的个数，大于等于极大堆数的个数
        #因此，在他们程度相等时，数先入极大堆，在从极大推pop一个传给极小堆
        if len(self.min_stack)==len(self.max_stack):
            heapq.heappush(self.max_stack,-num)
            heapq.heappush(self.min_stack,-heapq.heappop(self.max_stack))
        else:
            heapq.heappush(self.min_stack,num)
            heapq.heappush(self.max_stack,-heapq.heappop(self.min_stack))


    def findMedian(self) -> float:
        if len(self.min_stack)==len(self.max_stack):
            return (self.min_stack[0]-self.max_stack[0])/2
        else:
            return self.min_stack[0]
