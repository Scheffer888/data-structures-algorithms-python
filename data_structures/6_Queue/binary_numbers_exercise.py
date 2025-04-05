
from collections import deque

class dQueue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def front(self):
        if len(self.buffer) != 0:
            return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    

def print_binary(end):
    queue = dQueue()
    queue.enqueue('1')

    for i in range(end):
        binary_number = queue.dequeue()
        print('   ' + binary_number)

        queue.enqueue(binary_number + '0')
        queue.enqueue(binary_number + '1')

# Using queue python library
from queue import Queue
def print_binary_2(end):
    queue = Queue()
    queue.put('1')

    for i in range(end):
        binary_number = queue.get()
        print('   ' + binary_number)

        queue.put(binary_number + '0')
        queue.put(binary_number + '1')

    
if __name__ == '__main__':

    print_binary(12)
    print()
    print_binary_2(12)