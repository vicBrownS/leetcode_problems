"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-10^6 <= Node.val <= 10^6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        Reorganiza una lista enlazada agrupando primero los nodos en posiciones impares
        y luego los nodos en posiciones pares. La primera posición se considera 1 (impar).

        El algoritmo separa los nodos en dos listas enlazadas durante un único recorrido:
        una para los nodos impares y otra para los pares. Luego, conecta el final de la
        lista impar con el inicio de la lista par.

        Se mantiene el orden relativo original dentro de ambos grupos.

        Complejidad:
        - Tiempo: O(n), recorriendo la lista una sola vez.
        - Espacio: O(1), sin estructuras adicionales.

        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head  # Lista vacía o de 1 elemento, no hay nada que reordenar

        odd = head
        even = head.next
        even_head = even  # Guardamos el inicio de la lista par

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head  # Unimos al final de la lista impar, el inicio de la lista par
        return head

