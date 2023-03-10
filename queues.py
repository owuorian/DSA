# Queue follows the First in first Out (FIFO) rule
# the item that goes in first is the the item that comes out first

# Queue implementation in Python 

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

# Queue instance

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q .dequeue()

print('After removing an element')
q.display()

# Circular Queue implementation in Python

class CircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print('The circular queue is full\n')

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else: 
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print('The circular queus is empty\n')

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if (self.head == -1):
            print('No element in the circular queue')
        
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=' ')
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=' ')
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=' ')
            print()

# CircularQueue instance
obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

print('Initial queue')
obj.printCQueue()

obj.dequeue()
print('After removing an element from the queue')
obj.printCQueue()

