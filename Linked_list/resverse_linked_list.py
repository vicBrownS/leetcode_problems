"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        Invierte una lista enlazada simple y devuelve el nuevo nodo head.

        El algoritmo utiliza tres punteros:
        - `ant` (anterior): inicialmente None, almacenará el nodo anterior al actual.
        - `cur` (actual): recorre la lista nodo a nodo.
        - `next`: guarda temporalmente el siguiente nodo antes de invertir el enlace.

        En cada iteración del bucle:
        1. Se guarda el siguiente nodo (`next = cur.next`).
        2. Se invierte el puntero (`cur.next = ant`).
        3. Se avanza: `ant` pasa a ser `cur`, y `cur` pasa a ser `next`.

        Cuando `cur` llega a None, `ant` apunta al nuevo head de la lista invertida,
        que es el nodo que se retorna.

        Complejidad:
        - Tiempo: O(n), donde n es el número de nodos.
        - Espacio: O(1), uso constante de memoria.

        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ant = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = ant
            ant = cur
            cur = next
        return ant