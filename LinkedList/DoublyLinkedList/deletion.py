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
                if temp.next:
                    new_node.next.prev=new_node
                else:
                    self.tail=new_node
                temp.next = new_node
    def deletion(self,location):
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                target= curNode.next
                if target:
                    curNode.next = target.next
                    if target.next:
                        target.next.prev = curNode
                    else:
                        self.tail=curNode
            print("The node has been successfully deleted")

doublyLinkedList=DoublyLinkedList()
doublyLinkedList.creation(5)
doublyLinkedList.insertion(4,0)
doublyLinkedList.insertion(7,1)

doublyLinkedList.insertion(6,3)

doublyLinkedList.insertion(6,4)

doublyLinkedList.insertion(6,5)

doublyLinkedList.deletion(0)
doublyLinkedList.deletion(1)
doublyLinkedList.deletion(2)
print([temp.value for temp in doublyLinkedList])