"""
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Constraints:

1 <= n <= 8
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        Generates all structurally unique BSTs that store values 1...n.

        Args:
            n (int): Number of nodes with unique values from 1 to n.

        Returns:
            List[Optional[TreeNode]]: List of all unique BST roots.
        """
        if n == 0:
            return []

        def generate(start, end):
            trees = []
            if start > end:
                return [None]

            for i in range(start, end + 1):
                # Generate all possible left and right subtrees
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)

                # Combine them with root = i
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)

            return trees

        return generate(1, n)


