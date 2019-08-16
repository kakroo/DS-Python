class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #  This is for BST
    def add_BST(self, node):
        if self is None:
            self = node
        if node.data < self.data:
            add_BST(self.left, node)
        if node.data > self.data:
            add_BST(self.right, node)
        if node.data == self.data:
            print('Cannot ADD. Value already exists in BST')

    # TODO: 
    def inOrderTraversal(self):
