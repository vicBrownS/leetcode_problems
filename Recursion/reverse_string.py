"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:

1 <= s.length <= 10^5
s[i] is a printable ascii character.
"""


class Solution(object):
    def reverseString(self, s):
        """
        Reverses the input list of characters in-place using recursion.

        Args:
            s (List[str]): The input list of characters to reverse.

        Returns:
            None: The input list is modified in-place with O(1) extra memory.

        The function uses a helper recursive approach that swaps characters
        from the outer edges moving inward, until all elements are reversed.
        """

        def reverse(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)

        reverse(0, len(s) - 1)
