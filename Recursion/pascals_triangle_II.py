"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Constraints:

0 <= rowIndex <= 33
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        Recursively returns the `rowIndex`-th row (0-indexed) of Pascal's triangle.

        Args:
            rowIndex (int): The index of the desired row in Pascal's triangle.

        Returns:
            List[int]: The values of the row at position `rowIndex`.

        Each number is the sum of the two numbers directly above it in the previous row.
        This solution builds the triangle recursively from the top until reaching the desired row.
        """
        if rowIndex == 0:
            return [1]

        prev = self.getRow(rowIndex - 1)
        row = [1]  # first element is always 1
        for i in range(1, len(prev)):
            row.append(prev[i - 1] + prev[i])
        row.append(1)  # last element is always 1
        return row



