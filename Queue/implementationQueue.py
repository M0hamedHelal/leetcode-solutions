class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        dequeued_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_node.data

    def is_empty(self):
        return self.head is None


my_queue = Queue()
my_queue.enqueue("Customer 1")
my_queue.enqueue("Customer 2")

print("Served from queue:", my_queue.dequeue())