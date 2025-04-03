"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Devuelve el nodo en el que se intersectan dos listas enlazadas simples,
        o None si no se intersectan.

        Este algoritmo recorre ambas listas con dos punteros. Cuando un puntero
        llega al final de su lista, comienza a recorrer la otra. De esta forma,
        ambos punteros recorren la misma cantidad total de nodos (longitudA + longitudB).

        Si las listas se intersectan, se encontrarán en el nodo común después de
        como máximo dos recorridos. Si no se intersectan, ambos llegarán a None
        al mismo tiempo.
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        a,b = headA,headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a