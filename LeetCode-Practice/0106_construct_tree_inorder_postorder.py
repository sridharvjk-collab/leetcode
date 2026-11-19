# LeetCode 106. Construct Binary Tree from Inorder and Postorder Traversal
# Language: Python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        positions = {value: i for i, value in enumerate(inorder)}
        self.index = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            value = postorder[self.index]
            self.index -= 1
            node = TreeNode(value)
            middle = positions[value]

            node.right = build(middle + 1, right)
            node.left = build(left, middle - 1)
            return node

        return build(0, len(inorder) - 1)
