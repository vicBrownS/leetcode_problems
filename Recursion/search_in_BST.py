"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node = root
        if node.val == val:
            return node
        else:
            if node.left and node.right:
                return self.searchBST(node.left, val) or self.searchBST(node.right, val)
            elif node.left:
                return self.searchBST(node.left, val)
            elif node.right:
                return self.searchBST(node.right, val)
            else:
                return None
