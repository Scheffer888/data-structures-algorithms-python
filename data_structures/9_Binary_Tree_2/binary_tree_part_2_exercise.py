from collections import deque

class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:    
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def dfs_in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.dfs_in_order_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.dfs_in_order_traversal()

        return elements

    def dfs_pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.dfs_pre_order_traversal()
        
        if self.right:
            elements += self.right.dfs_pre_order_traversal()

        return elements

    def dfs_post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.dfs_post_order_traversal()
        
        if self.right:
            elements += self.right.dfs_post_order_traversal()
        
        elements.append(self.data)

        return elements
    
    def bfs_traversal(self):
        elements = []
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current_node = queue.popleft()
            elements.append(current_node.data)

            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)

        return elements
            
    
    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
            
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
            
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_max()

    def calculate_sum(self):
        return sum(self.dfs_in_order_traversal())
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
    
    def delete_alt(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.right.delete(max_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__ == '__main__':

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("DFS - in order traversal:", numbers_tree.dfs_in_order_traversal())
    print("BFS - traversal:", numbers_tree.bfs_traversal())
    numbers_tree.delete_alt(20)
    print("After deleting 20: ", numbers_tree.dfs_in_order_traversal())




