"""
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        Elimina todos los nodos de una lista enlazada simple cuyo valor sea igual a `val`,
        y devuelve el nuevo head de la lista.

        Utiliza un nodo ficticio (`dummy`) al principio para facilitar la eliminación
        del nodo head, si es necesario. Luego recorre la lista con dos punteros:
        - `prev`: apunta al último nodo no eliminado.
        - `current`: nodo actual que se está evaluando.

        Si `current.val == val`, se omite ajustando `prev.next`.
        Si no, se avanza `prev`.

        Complejidad:
        - Tiempo: O(n), donde n es el número de nodos.
        - Espacio: O(1), sin estructuras auxiliares.
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            if current.val == val:
                prev.next = current.next  # Omitimos el nodo
            else:
                prev = current  # Solo avanzamos prev si no lo eliminamos
            current = current.next

        return dummy.next


