class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def insert_after(self, target_data, new_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def delete_head(self):
        if self.head is None:
            return None
        removed_node = self.head
        self.head = self.head.next
        return removed_node.data
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def delete_tail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_node = self.head
            self.head = None
            return removed_node.data
        current = self.head
        while current.next.next:
            current = current.next
        removed_node = current.next
        current.next = None
        return removed_node.data
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////    
    def get_last(self):
        if self.head is None:
            return None

        current = self.head

        while current.next:
            current = current.next
        return current.data
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def get_first(self):
        if self.head is None:
            return None
        return self.head.data 
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////    
    def clear(self):
        self.head = None
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////       
    def is_empty(self):
        
        return self.head is None    
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(" -> ".join(result))

# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
my_list = LinkedList()
my_list.append("Data A")
my_list.append("Data B")
my_list.append("Data C")

my_list.insert_after("Data A", "Data X")
my_list.print_list()

my_list.delete_head()
my_list.print_list()

my_list.delete_tail()
my_list.print_list()