from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # O(N)
    def getLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # O(1)
    def addNodeStart(self, data):
        # Create new Node obj with the data
        newNode = Node(data)
        # assign the current head to the new node next
        newNode.next = self.head
        # Assign the initial head to the new node
        self.head = newNode

    # # O(N)
    # def addNodeEnd(self, data):
    #     # Create new node from the given data
    #     newNode = Node(data)

    #     temp = self.head
    #     while temp:
    #         if temp.next is None:
    #             temp.next = newNode
    #         break
