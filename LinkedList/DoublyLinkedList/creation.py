class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev= None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp=temp.next

    def creation(self,value):
        new_node=Node(value)
        new_node.next=None
        new_node.prev=None
        self.head=new_node
        self.tail=new_node

doublyLinkedList=DoublyLinkedList()
doublyLinkedList.creation(5)
print([temp.value for temp in doublyLinkedList])