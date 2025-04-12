"""
Given the head of a linked list, rotate the list to the right by k places.

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # 1. Calcular longitud y encontrar último nodo
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Hacer que la lista sea circular
        tail.next = head

        # 3. Calcular el nuevo punto de ruptura
        k = k % length
        steps_to_new_head = length - k

        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Romper el ciclo

        return new_head


