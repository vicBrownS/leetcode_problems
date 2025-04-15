"""
We build a table of n rows (1-indexed).
We start by writing 0 in the 1st row.
Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01,
and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
"""
class Solution(object):
    def kthGrammar(self, n, k):
        """
        Returns the k-th symbol in the n-th row of the grammar table.

        Args:
            n (int): The row number (1-indexed).
            k (int): The position in the row (1-indexed).

        Returns:
            int: The symbol at position k in row n.

        The sequence is defined recursively, and each level doubles in size.
        We avoid generating the full row and instead determine the k-th symbol
        by recursively examining its parent in the previous row.
        """
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)

        is_k_even = (k % 2 == 0)

        if parent == 0:
            return 1 if is_k_even else 0
        else:
            return 0 if is_k_even else 1

