class Queue:
    def __init__(self):
        self.items=[]
    def __str__(self):
        values = [str(x) for x in self.items]
        return  " ".join(values)

    def isEmpty(self):
        if self.items==[]:
            return " the queue is empty"

    def enqueue(self,value):
        self.items.append(value)
        return value

    def dequeue(self):
        if self.isEmpty():
            return "the queue is empty"
        else:
            self.items.pop(0)
    def peek(self):
        return self.items[0]

    def delete(self):
        self.items=[]

custom_queue=Queue()
print(custom_queue.isEmpty())
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
print(custom_queue)
custom_queue.dequeue()
print(custom_queue)
print(custom_queue.peek())
custom_queue.delete()
print(custom_queue)

