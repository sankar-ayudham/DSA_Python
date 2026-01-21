

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

    def insertion(self,value,location):
        if self.head is None:
            return  "the DLL doesnt exit"
        else:
            new_node=Node(value)
            if location==0:
                new_node.prev=self.tail
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
                self.tail.next=new_node
            elif location ==1:
                new_node.next =self.head
                new_node.prev=self.tail
                self.head.prev = new_node
                self.tail.next= new_node
                self.tail=new_node

            else:
                temp = self.head
                index=0
                while index < location-1:
                    temp=temp.next
                    index+=1
                new_node.next = temp.next
                new_node.prev=temp
                new_node.next.prev=new_node
                temp.next=new_node
    def reversal(self):
        temp =self.tail
        while temp:
            print(temp.value)
            temp=temp.prev
            if temp==self.tail:
                break
# Create instance
my_circularL_linked_list = CirculardoubleLinkedList()
print(my_circularL_linked_list.creation(5))

my_circularL_linked_list.insertion(1,0)
my_circularL_linked_list.insertion(8,1)
my_circularL_linked_list.insertion(2,5)
my_circularL_linked_list.insertion(1,0)
my_circularL_linked_list.insertion(7,1)
my_circularL_linked_list.insertion(2,5)
my_circularL_linked_list.reversal()

# Print values in the circular doubly linked list
print([temp.value for temp in my_circularL_linked_list])

