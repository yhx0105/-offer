#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:hello_life 
@license: Apache Licence 
@file: 01_序列化二叉树.py 
@time: 2020/12/12
@software: PyCharm 
description:请实现两个函数，分别用来序列化和反序列化二叉树。
"""
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        BFS
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        deq=collections.deque()
        deq.append(root)
        res=[]
        while deq:
            node=deq.popleft()
            if node:
                res.append(str(node.val))
                # 因为结果有null 所以不判定node左右节点是否为空
                deq.append(node.left)
                deq.append(node.right)
            else:
                res.append("null")
        return "["+",".join(res)+"]"



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data=="[]":
            return
        vals,i=data[1:-1].split(","),1
        root=TreeNode(int(vals[0]))
        que=collections.deque()
        que.append(root)
        while que:
            node=que.popleft()
            if vals[i]!='null':
                node.left=TreeNode(vals[i])
                que.append(node.left)
            i+=1
            if vals[i]!='null':
                node.right=TreeNode(vals[i])
                que.append(node.right)
            i+=1
        return root






