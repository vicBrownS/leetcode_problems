class MyLinkedList(object):
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.first = None

    def get(self, index):
        """
        Devuelve el valor del nodo en la posición index de la lista.
        Si el índice es inválido, devuelve -1.
        """
        if index < 0:
            return -1

        current = self.first
        for _ in range(index):
            if current is None or current.next is None:
                return -1
            current = current.next

        return current.value if current else -1

    def addAtHead(self, val):
        """
        Inserta un nodo con valor `val` al inicio de la lista.
        """
        node = self.Node(val)

        if self.first is None:
            self.first = node
        else:
            node.next = self.first
            self.first.prev = node
            self.first = node

    def addAtTail(self, val):
        """
        Inserta un nodo con valor `val` al final de la lista.
        """
        node = self.Node(val)

        if self.first is None:
            self.first = node
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

    def addAtIndex(self, index, val):
        """
        Inserta un nodo con valor `val` antes del nodo en la posición `index`.
        Si index es 0, se inserta al principio.
        Si index == longitud, se inserta al final.
        Si index > longitud, no se inserta nada.
        """
        if index < 0:
            raise ValueError("Index can't be negative")

        # Si insertamos al principio
        if index == 0:
            self.addAtHead(val)
            return

        current = self.first
        for _ in range(index - 1):
            if current is None:
                return  # Index fuera de rango
            current = current.next
        if current is None:
            return
        # Si estamos al final, o index == length
        if current is not None and current.next is None:
            self.addAtTail(val)
        else:
            new_node = self.Node(val)
            next_node = current.next

            current.next = new_node
            new_node.prev = current

            new_node.next = next_node
            next_node.prev = new_node

    def deleteAtIndex(self, index):
        """
        Elimina el nodo en la posición `index`, si existe.
        """
        if index < 0:
            return

        cur = self.first
        for _ in range(index):
            if cur is None:
                return
            cur = cur.next

        if cur is None:
            return

        if cur.prev is None:
            # Eliminando el primer nodo
            self.first = cur.next
            if self.first:
                self.first.prev = None
        elif cur.next is None:
            # Eliminando el último nodo
            cur.prev.next = None
        else:
            # Nodo en medio
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
