class MyLinkedList(object):

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.first = None
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the indexth node in the linked list.
        If the index is invalid, return -1
        :type index: int
        :rtype: int
        """
        #Check for invalid index
        if index < 0:
            raise ValueError('Index must be greater than or equal to 0.')

        #If the linkedlist len is 0
        if self.first is None:
            return -1

        #Set head to first
        self.head = self.first
        it = 0

        #While the index doesn`t march the number of iterations
        while index != it:
            #If the end is reached return -1
            if self.head.next is None:
                return -1
            self.head = self.head.next
            it += 1
        #Return the actual head value
        return self.head.value

    def addAtHead(self, val: int) -> None:
        """
            Add a node of value val before the first element of the linked list.\n
            After the insertion, the new node will be the first node of the linked list.
            :type val: int
            :rtype: None
        """
        # Set head to first
        self.head = self.first
        # If the linkedlist is empty add to first
        if self.head is None:
            self.first = self.Node(val)
        else:
            #Adds the node at the beggining of the list
            self.first = self.Node(val)
            self.first.next = self.head


    def addAtTail(self, val: int) -> None:
        """
         Append a node of value val as the last element of the linked list.
        :type val: int
        :rtype: None
        """
        # Set head to first
        self.head = self.first
        # If the linkedlist is empty add to first
        if self.head is None:
            self.first = self.Node(val)
        else:
            # If the head node isn´t the last one
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = self.Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the indexth node in the linked list.
        If index equals the length of the linked list,
        the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        # Check for invalid index
        if index < 0:
            raise ValueError('Index must be greater than or equal to 0.')
        # Set head to first
        anterior = None
        self.head = self.first
        it = 0
        #new_node
        new_node = self.Node(val)
        #While the index doesn`t march the number of iterations
        while index != it:
            #If the end is reached break while loop
            if self.head is None or self.head.next is None :
                break
            #Iterate over the next node and iterator value
            anterior = self.head
            self.head = self.head.next
            it += 1
        #After the loop two situations can happen:
        #The next head is None which means index >= length so either index = length and node is inserted
        # on the tail or index > length so node isn`t inserted.
        #The next head is not None which means the Node has to be inserted in the middle of two others.
        if not(self.head is None and it != index):
            if self.head is None:
                self.first = new_node
                self.head = self.first
            elif self.head.next is None:
                if it == index:
                    new_node.next = self.head
                    if anterior is not None:
                        anterior.next = new_node
                    else:
                        self.first = new_node
                if it + 1 == index:
                    self.head.next = new_node
            else:
                new_node.next = self.head
                anterior.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the indexth node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        # Check for invalid index
        if index < 0:
            raise ValueError('Index must be greater than or equal to 0.')
        # Set head to first
        self.head = self.first
        anterior = None
        it = 0
        # While the index doesn`t march the number of iterations
        while index != it:
            #If the current head is None, end is reached so break the while loop
            if self.head is None:
                break
            anterior = self.head
            self.head = self.head.next
            it += 1
        #If list is empty anterior is None and self.head is None, no removes
        #If list has 1 element and index 0 anterior is None and self.head is not None, remove 0
        #If list has any elements and index out of bounds, anterior is not None and self.head is None, no removes
        #Any other case anterior is Not None and self.head is not None, remove index
        if anterior is not None and self.head is not None:
            anterior.next = self.head.next
        elif anterior is None and self.head is not None:
            if self.head.next is None:
                self.first = None
                self.head = None
            else:
                self.first = self.head.next
    def printList(self):
        self.head = self.first
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print("LinkedList:", values)


ll = MyLinkedList()
ll.addAtIndex(1,0)
ll.get(0)
ll.addAtHead(38)
ll.addAtTail(66)
ll.addAtTail(61)
ll.addAtTail(76)
ll.addAtTail(26)
ll.addAtTail(37)
ll.addAtTail(8)
ll.deleteAtIndex(5)      # Eliminar nodo en posición 5
ll.addAtHead(4)
ll.addAtHead(45)
print(ll.get(4))                # Esperado: 61
ll.addAtTail(85)
ll.addAtHead(37)
print(ll.get(5))               # Esperado: 61
ll.addAtTail(93)
ll.addAtIndex(10, 23) # Insertar 23 en posición 10
ll.addAtTail(21)
ll.addAtHead(52)
ll.addAtHead(15)
ll.addAtHead(47)
ll.printList()
print(ll.get(12))              # Esperado: 85
ll.addAtIndex(6, 24)
ll.printList()
ll.addAtHead(64)
print(ll.get(4) )               # Esperado: 37
ll.addAtHead(31)
ll.deleteAtIndex(6)
ll.addAtHead(40)
ll.addAtTail(17)
ll.addAtTail(15)
ll.addAtIndex(19, 2)     # <--- ¡Esta inserción es clave!
ll.addAtTail(11)
ll.addAtHead(86)
print(ll.get(17))        # ❌ Devuelve 93, esperado: 23
