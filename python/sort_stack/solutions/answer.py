%run ../stack/stack.py
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
