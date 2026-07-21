class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def delete(self, data):
        if self.head is None:
            return False
        current = self.head
        previous = None
        while True:
            if current.data == data:
                if previous is None:
                    if current.next == self.head:
                        self.head = None
                    else:
                        tail = self.head
                        while tail.next != self.head:
                            tail = tail.next
                        self.head = current.next
                        tail.next = self.head
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
            if current == self.head:
                break
        return False
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def print_list(self, count=10):
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        result = []
        for _ in range(count):
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(result) + " -> (back to head)")
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////

cll = CircularLinkedList()
cll.append("Data A")
cll.append("Data B")
cll.append("Data C")

cll.print_list()

cll.delete("Data B")
cll.print_list()