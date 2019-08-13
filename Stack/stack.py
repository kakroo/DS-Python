class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        isEmpty = len(self.stack) == 0
        print(isEmpty)
        return isEmpty

    def push(self, data):
        self.stack.append(data)
        print("{} pushed to stack".format(data))

    def pop(self):
        if self.isEmpty():
            print("Cannot Pop as Stack is Empty")
            return
        last = self.stack[-1]
        del self.stack[-1]
        print("{} popped from Stack".format(last))

    def peek(self):
        if self.isEmpty():
            print("Cannot Peek as Stack is Empty")
            return
        print("Peeked and found {}".format(self.stack[-1]))

    def traverse(self):
        rev = reversed(self.stack)
        print("Current Stack Data")
        for element in rev:
            print(element)
