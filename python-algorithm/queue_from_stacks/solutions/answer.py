class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None


class QueueFromStacks(object):
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def shift_stacks(self, source, destination):
        while source.peek() is not None:
            destination.push(source.pop())

    def enqueue(self, data):
        self.shift_stacks(self.right_stack, self.left_stack)
        self.left_stack.push(data)

    def dequeue(self):
        self.shift_stacks(self.left_stack, self.right_stack)
        return self.right_stack.pop()
