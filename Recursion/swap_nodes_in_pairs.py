"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        Recursively swaps every two adjacent nodes in a singly linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the modified list with every two nodes swapped.

        The function swaps the first two nodes, then recursively swaps the rest of the list,
        connecting the swapped pairs together. The values in the nodes are not modified,
        only the node links are changed.
        """
        if head is None or head.next is None:
            return head

        first = head
        second = head.next

        # Recursively swap the rest
        first.next = self.swapPairs(second.next)
        # Swap current pair
        second.next = first

        # New head is the second node
        return second
