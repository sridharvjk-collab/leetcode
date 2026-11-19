# LeetCode 99. Recover Binary Search Tree
# Language: Python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.previous = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)

            if self.previous and self.previous.val > node.val:
                if self.first is None:
                    self.first = self.previous
                self.second = node

            self.previous = node
            inorder(node.right)

        inorder(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
