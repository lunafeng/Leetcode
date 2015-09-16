#!/usr/bin/python
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def levelOrder(self, root):
        output = []
        if root is None:
            return []
        q = [root]
        while len(q):
            level = []
            for e in q:
                level.append(e.val)
            output.append(level)
            q2 = []
            for x in q:
                if x.left is not None:
                    q2.append(x.left) 
                if x.right is not None:
                    q2.append(x.right) 
            q = q2
        return output 
                

root = TreeNode(3)
left1 = TreeNode(9)
right1 = TreeNode(20)
left2 = TreeNode(15)
right2 = TreeNode(7)
root.left = left1
root.right = right1
right1.left = left2
right1.right = right2
test = Solution()
print test.levelOrder(root)



