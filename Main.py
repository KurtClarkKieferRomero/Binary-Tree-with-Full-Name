class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

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


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)  # in order or in the middle of the list that the root node is placed

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]  # this is to put the Root node at the first list
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

        elements.append(self.data)  # after all the data has been traversed, the root node is displayed

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.Right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

    def find_max(self):  # This will continue to go the right subtree to find the max value
        if self.right is None:
            return self.data
        return self.right.find_max()






def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    full_name = ['K', 'U', 'R', 'T', 'C', 'L', 'A', 'R', 'K', 'K', 'I', 'E', 'F', 'E', 'R', 'K', 'R', 'O', 'M', 'E', 'R', 'O']

    name_tree = build_tree(full_name)

    print("In In-order traversal: ", name_tree.in_order_traversal())
    print("In Pre-order traversal: ", name_tree.pre_order_traversal())
    print("In Post-order traversal: ", name_tree.post_order_traversal())



