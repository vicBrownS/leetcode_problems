"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        Computes the maximum depth of a binary tree using recursion.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The maximum depth (number of nodes from root to the deepest leaf).

        The function recursively computes the depth of the left and right subtrees,
        then returns the greater of the two plus one for the current node.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


