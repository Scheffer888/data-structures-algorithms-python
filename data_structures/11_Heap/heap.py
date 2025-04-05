'''
# Heap

### What is a Heap?
- A heap is a complete binary tree that satisfies the heap property.
- The heap property states that the key stored in each node is either greater than or equal to (≥) - for a maxheap - or
    less than or equal to (≤) - for a min heap - the keys in the node's children, according to some total order.    

### Python Library:
- Python has a built-in library called heapq from that provides heap data structure. Ex.:
import heapq

### Time Complexity:

    - insert: O(log n)
    - get_min: O(1)
    - extract_min: O(log n)
    - update: O(log n) if we have the index, O(n) if we don't
    - build: O(n)

'''

class MinHeap:
    def __init__(self, arr=None): # Heapifies the array in O(n) time
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap)//2-1, -1, -1):
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        minval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return minval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new < old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)

class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i] < self.heap[right]):
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            i = biggest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        maxval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return maxval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new > old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)


def heapsort(arr):
    heap = MinHeap(arr)
    return [heap.extract_min() for i in range(len(heap.heap))]


class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap()

    def enqueue(self, element): # Time complexity is O(log n)
        self.queue.insert(element)

    def peek(self): # Time complexity is O(1)
        return self.queue.get_max()

    def dequeue(self, element): # Time complexity is O(log n)
        return self.queue.extract_max()

    def is_empty(self): # Time complexity is O(1)
        return len(self.queue.heap) == 0

    def change_priority_by_index(self, i, new): # Time complexity is O(log n) if we have the index
        self.queue.update_by_index(i, new)

    def change_priority(self, old, new): # Time complexity is O(n) if we don't have the index
        self.queue.update(old, new)

import heapq

if __name__ == '__main__':
    arr = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

    # Using the custom MinHeap class
    minheap = MinHeap(arr)
    print('Heapmin using the custom MinHeap class:\n', minheap.heap)
    minn = minheap.extract_min()
    print('Min value', minn)
    
    print()
    # Using the built-in heapq library
    arr2 = arr.copy()
    heapq.heapify(arr2)
    print('Heapmin using heapq:\n', arr2)
    minnim = heapq.heappop(arr2)
    print('Min value: ', minnim)
    sorted_arr = [heapq.heappop(arr2) for i in range(len(arr2))]
    print('Sorted array using heapify: ', sorted_arr)

    print()
    # Using the custom MaxHeap class
    maxheap = MaxHeap(arr)
    print('Heapmax using the custom MaxHeap class:\n', maxheap.heap)
    maxn = maxheap.extract_max()
    print('Max value: ', maxn)

    print()
    # Using the built-in heapq library
    arr3 = [-x for x in arr]
    heapq.heapify(arr3)
    print('Heapmax with neg sign using heapq:\n', arr3)
    maxn = -heapq.heappop(arr3)
    print('Max value: ', maxn)
    sorted_arr = [-heapq.heappop(arr3) for i in range(len(arr3))]




