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
    def insertion(self,value , location):
        if self.head is None:
            print("we cant insert node")
        else:
            new_node=Node(value)
            if location==0:
                new_node.prev=None
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
            elif location ==1:
                new_node.next=None
                new_node.prev=self.tail
                self.tail.next=new_node
                self.tail=new_node
            else:
                temp = self.head
                index=0
                while index <location-1:
                    temp=temp.next
                    index+=1
                new_node.next=temp.next
                new_node.prev=temp
                new_node.next.prev=new_node
                temp.next = new_node
    def traversal(self):
        if self.head is None:
            return "no double linked list"
        else:
            temp=self.head
            while temp is not None:
                print(temp.value)
                temp=temp.next

doublyLinkedList=DoublyLinkedList()
doublyLinkedList.creation(5)
doublyLinkedList.insertion(4,0)
doublyLinkedList.insertion(7,1)
doublyLinkedList.insertion(6,2)
doublyLinkedList.traversal()

print([temp.value for temp in doublyLinkedList])