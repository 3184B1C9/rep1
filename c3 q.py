from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Usage Example
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", list(queue.queue))  
print("Front element:", queue.peek())  
print("Dequeued element:", queue.dequeue())  
print("Queue after dequeue:", list(queue.queue)) 
