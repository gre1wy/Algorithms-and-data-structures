class CircularQueue_array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue item.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue item.")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue_list:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue item.")
            return
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue item.")
            return None
        item = self.front.data
        if self.size == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        print("Queue:", end=" ")
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.front:
                break
        print()


# Приклад використання:
cq = CircularQueue_list(5)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()  # Output: Queue: 1 2 3 4 5

print("Dequeue:", cq.dequeue())  # Output: Dequeue: 1

cq.enqueue(6)
cq.display()  # Output: Queue: 2 3 4 5 6
