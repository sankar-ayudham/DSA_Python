class Node:
    def __init__(self,value =None):
        self.value = value
        self.next =None

class CircularsingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            if temp.next==self.head:
                break
            temp.next=temp

    def createCircularSingular(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        new_node.next=new_node

circularlinkedlist=CircularsingleLinkedList()
circularlinkedlist.createCircularSingular(5)

print([temp.value for temp in circularlinkedlist])