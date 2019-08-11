class LinkedList:
    def __init__(self):
        self.head = None

    # O(N)
    def getLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
