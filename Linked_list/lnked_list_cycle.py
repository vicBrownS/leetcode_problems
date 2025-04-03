"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Comprueba si hay un bucle haciendo uso de los constrains.
        Como el número máximo de nodos es 10000 si se itera un número
        de veces mayor a 10000 significa que hay un bucle, en caso
        contrario no lo hay.
        :type head: ListNode
        :rtype: bool
        """
        count = 0
        if head is None:
            return False
        while head is not None:
            head = head.next
            count += 1
            if count > 10000:
                return True
        return False