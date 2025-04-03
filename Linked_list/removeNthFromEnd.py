"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Elimina el n-ésimo nodo desde el final de una lista enlazada y devuelve el head actualizado.

        Se utiliza un nodo ficticio (dummy) al inicio de la lista para simplificar casos donde
        se debe eliminar el primer nodo. Luego, se aplican dos punteros:

        - Uno se adelanta n+1 pasos (puntero rápido).
        - El otro (puntero lento) comienza desde el dummy y avanza junto al rápido hasta que este llegue al final.

        En ese momento, el puntero lento está justo antes del nodo a eliminar. Se ajusta su `next`
        para saltarse dicho nodo.

        Complejidad:
        - Tiempo: O(L), siendo L la longitud de la lista.
        - Espacio: O(1), sin estructuras auxiliares.

        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        foward = dummy

        # Mover foward n+1 pasos adelante
        for _ in range(n + 1):
            foward = foward.next

        # Mover ambos punteros hasta que foward llegue al final
        while foward:
            start = start.next
            foward = foward.next

        # Eliminar el nodo siguiente al puntero lento
        start.next = start.next.next

        return dummy.next  # En caso de que el head original se haya eliminado
