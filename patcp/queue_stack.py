class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return "Queue is empty"
            else:
                while self.stack_enqueue:
                    self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def peek(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return "Queue is empty"
            else:
                while self.stack_enqueue:
                    self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]

    def is_empty(self):
        return not self.stack_enqueue and not self.stack_dequeue

# Testing the QueueUsingStacks implementation
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Peek:", queue.peek())  # Should print 1
print("Dequeue:", queue.dequeue())  # Should remove and print 1
print("Peek after dequeue:", queue.peek())  # Should print 2
print("Is queue empty?", queue.is_empty())  # Should print False

print("Dequeue:", queue.dequeue())  # Should remove and print 2
print("Dequeue:", queue.dequeue())  # Should remove and print 3
print("Is queue empty?", queue.is_empty())  # Should print True
print("Dequeue from empty queue:", queue.dequeue())  # Should print "Queue is empty"
