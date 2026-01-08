class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


class SingleLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        temp= self.head
        while temp:
            yield temp
            temp=temp.next

    def insertion(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif location == 0:
            new_node.next = self.head
            self.head = new_node
        elif location == 1:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            temp = self.head
            index = 0
            while index < location - 1:
                temp = temp.next
                index += 1
            nextnode = temp.next
            temp.next = new_node
            new_node.next = nextnode

    def search(self,value):
        if self.head is None:
            print("the linked list is empty")
        else:
            temp=self.head
            while temp is  not None:
                if temp.value==value:
                    return temp.value
                temp=temp.next
            return "the element you are looking for doesnt exist"

my_linked_list = SingleLinkedlist()
my_linked_list.insertion(1, 0)
my_linked_list.insertion(2, 1)
my_linked_list.insertion(2, 1)
my_linked_list.insertion(2, 1)
my_linked_list.insertion(5, 2)
print(my_linked_list.search(5))
print([temp.value for temp in my_linked_list])
