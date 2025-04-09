"""
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer.
This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.
These child lists may have one or more children of their own, and so on,
to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list,
flatten the list so that all the nodes appear in a single-level,
doubly linked list. Let curr be a node with a child list.
The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list.
The nodes in the list must have all of their child pointers set to null.
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        Aplana una lista doblemente enlazada multilevel en una sola lista doblemente enlazada.
        Los nodos hijos se insertan justo después de su nodo padre y antes del siguiente.
        """
        if not head:
            return None

        cur = head
        while cur:
            if cur.child:
                next_cur = cur.next

                # Aplanar la sublista recursivamente
                child_head = self.flatten(cur.child)

                # Insertar la sublista
                cur.next = child_head
                child_head.prev = cur
                cur.child = None  # Eliminar el puntero child

                # Conectar el final de la sublista al siguiente original
                tail = child_head
                while tail.next:
                    tail = tail.next

                tail.next = next_cur
                if next_cur:
                    next_cur.prev = tail

            cur = cur.next

        return head



