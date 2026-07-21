class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def print_forward(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" <-> ".join(result))
        
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////

    def print_backward(self):
        current = self.tail
        result = []
        while current:
            result.append(str(current.data))
            current = current.prev
        print(" <-> ".join(result))

# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
dll = DoublyLinkedList()
dll.append("Data A")
dll.append("Data B")
dll.append("Data C")

dll.print_forward()
dll.print_backward()

dll.delete("Data B")
dll.print_forward()