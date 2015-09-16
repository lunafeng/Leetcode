#!/usr/bin/python
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetric2(root.left, root.right)

    def isSymmetric2(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        return self.isSymmetric2(p.left, q.right) and self.isSymmetric2(p.right, q.left)
