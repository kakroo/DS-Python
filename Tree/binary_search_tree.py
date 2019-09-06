class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_BST(self, data):
        if data < self.data:
            if self.left:
                self.left.add_BST(data)
            else:
                self.left = BST(data)
        elif data > self.data:
            if self.right:
                self.right.add_BST(data)
            else:
                self.right = BST(data)
        else:
            print('Cannot Add {}, Value already exist in BST'.format(data))

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print("{}\n".format(self.data))
        if self.right:
            self.right.print_inorder()


def main():
    bst = BST(5)
    bst.add_BST(3)
    bst.add_BST(3)
    bst.add_BST(6)
    bst.add_BST(2)
    bst.print_inorder()


if __name__ == '__main__':
    main()
