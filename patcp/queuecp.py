class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            self.front = self.front.next

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("Queue elements:")
queue.display()
print("Front element:", queue.peek())
