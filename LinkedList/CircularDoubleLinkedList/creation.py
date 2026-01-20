class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CirculardoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
            if temp == self.head:
                break

    def creation(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        return "Circular doubly linked list created successfully"

# Create instance
my_circularL_linked_list = CirculardoubleLinkedList()
print(my_circularL_linked_list.creation(5))

# Print values in the circular doubly linked list
print([temp.value for temp in my_circularL_linked_list])

