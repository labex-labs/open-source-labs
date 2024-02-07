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


class Hanoi(object):
    def move_disks(self, num_disks, src, dest, buff):
        if src is None or dest is None or buff is None:
            raise TypeError("Cannot have a None input")
        self._move_disks(num_disks, src, dest, buff)

    def _move_disks(self, num_disks, src, dest, buff):
        if num_disks == 0:
            return
        self.move_disks(num_disks - 1, src, buff, dest)
        dest.push(src.pop())
        self.move_disks(num_disks - 1, buff, dest, src)
