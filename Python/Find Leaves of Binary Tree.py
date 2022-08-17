# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

import collections

class Solution:
    def findLeaves(self, root):
        def helper(root):
            if not root: return 0
            left = helper(root.left)
            right = helper(root.right)
            level = max(left, right) + 1
            dic[level] += root.val,
            return level
        dic = collections.defaultdict(list)
        helper(root)
        return list(dic.values())


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

ob = Solution()

ob.findLeaves(root)

        