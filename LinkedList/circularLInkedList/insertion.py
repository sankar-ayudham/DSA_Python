class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularsingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        if not self.head:
            return
        temp = self.head
        while True:
            yield temp
            temp = temp.next
            if temp == self.head:
                break

    def createCircularSingular(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node

    def insertion(self, value, location):
        if self.head is None:
            return "The linked list doesn’t exist"
        else:
            new_node = Node(value)
            if location == 0:  # Insert at beginning
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:  # Insert at end
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:  # Insert at specific location
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                    if temp == self.head:  # If location is too large
                        return "Location out of range"
                new_node.next = temp.next
                temp.next = new_node
            return "The node has been successfully created"

circularlinkedlist = CircularsingleLinkedList()
circularlinkedlist.createCircularSingular(5)
circularlinkedlist.insertion(5, 0)   # Insert at beginning
circularlinkedlist.insertion(10, 1)  # Insert at end
circularlinkedlist.insertion(6, 2)   # Insert at position 2
circularlinkedlist.insertion(8, 2)   # Insert at position 2

print([temp.value for temp in circularlinkedlist])
