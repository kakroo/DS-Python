from linkedList import LinkedList
from node import Node

# Linked list consists of nodes where each node contains a data field and a reference(link)
# to the next node in the list.

# CREATION

# Create an Linked List with an empty head
l_list = LinkedList()
# Assign the head to newly created node
l_list.head = Node(1)
# second = Node(2)
# third = Node(3)

# Assign 1st next to 2nd
# l_list.head.next = second # This can be replced by addNodeEnd

l_list.addNodeStart(10)
l_list.addNodeEnd(11)

# Then 2nd next to 3rd node.
# second.next = third

# TRAVERSAL
l_list.getLinkedList()
