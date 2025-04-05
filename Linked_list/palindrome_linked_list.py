"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        Determina si una lista enlazada es palíndroma comparando los valores
        desde los extremos hacia el centro, tras invertir la segunda mitad de la lista.
        Complejidad: O(n) tiempo, O(1) espacio.
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Encontrar el punto medio con slow/fast
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Invertir la segunda mitad
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Comparar ambas mitades
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True




