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

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

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
        return self.left.find_min()

    def calculate_sum(self):
        return sum(self.in_order_traversal())

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
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
