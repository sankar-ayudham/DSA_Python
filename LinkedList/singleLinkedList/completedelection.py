class Node:
    def __init__(self,value=None):
        self.value =value
        self.next=None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next

    def insertion(self,value,location):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        elif location==0:
            new_node.next=self.head
            self.head=new_node
        elif location ==1:
            self.tail.next=new_node
            self.tail=new_node
            new_node.next=None
        else:
            temp=self.head
            index=0
            while index<location-1:
                temp=temp.next
                index+=1
            nextnode=temp.next
            temp.next=new_node
            new_node.next=nextnode
    def completedelet(self):
        if self.head==None:
            print('the list doesnt exit')
        else:
            self.head=None
            self.tail=None


my_linked_list=SingleLinkedList()
my_linked_list.insertion(1,0)
my_linked_list.insertion(2,1)
my_linked_list.insertion(2,1)
my_linked_list.insertion(2,1)
my_linked_list.insertion(5,2)
my_linked_list.completedelet()
print([temp.value for temp in my_linked_list])