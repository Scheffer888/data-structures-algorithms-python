from collections import deque

class Stack():
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peak(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(string):
    stack = Stack()
    for c in string:
        stack.push(c)
    
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()
        
    return rev_str


if __name__ == '__main__':
    string = "We will conquer COVID-19"
    print(reverse_string(string))

