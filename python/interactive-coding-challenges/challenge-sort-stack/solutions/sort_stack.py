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


class MyStack(Stack):
    def sort(self):
        buff = MyStack()
        while not self.is_empty():
            temp = self.pop()
            if buff.is_empty() or temp >= buff.peek():
                buff.push(temp)
            else:
                while not buff.is_empty() and temp < buff.peek():
                    self.push(buff.pop())
                buff.push(temp)
        return buff


class MyStackSimplified(Stack):
    def sort(self):
        buff = MyStack()
        while not self.is_empty():
            temp = self.pop()
            while not buff.is_empty() and temp < buff.peek():
                self.push(buff.pop())
            buff.push(temp)
        return buff
