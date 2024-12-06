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

# Not optimal (below) -- see solution
def is_balanced(string):
    stack = Stack()

    pairs = [('(', ')'), ('[', ']'), ('{', '}')]

    for c in string:
        for start, end in pairs:
            if c == start:
                stack.push(c)
                break
            if c == end:
                if stack.is_empty():
                    return False
                else:
                    if stack.peak() == start:
                        stack.pop()
                    else:
                        return False
                        
    
    if not stack.is_empty():
        return False
    
    return True

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))") )
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))