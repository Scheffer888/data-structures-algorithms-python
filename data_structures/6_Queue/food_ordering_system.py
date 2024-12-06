from collections import deque
import threading
import time
import sys

class Queue():
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    

def place_order(orders):
    global queue
    for order in orders:
        print('Placing order for: ', order)
        queue.enqueue(order)
        time.sleep(0.5)

def serve_order():
    global queue
    time.sleep(1)
    while not queue.is_empty():
        print(queue.dequeue())
        time.sleep(2)



if __name__ == '__main__':

    queue = Queue()

    orders = ['pizza','samosa','pasta','biryani','burger']

    place_order_thread = threading.Thread(target=place_order, args=(orders,))
    serve_order_thread = threading.Thread(target=serve_order)

    place_order_thread.start()
    serve_order_thread.start()

    place_order_thread.join()
    serve_order_thread.join()
    sys.exit()