%run ../linked_list/linked_list.py
class MyLinkedList(LinkedList):

    def remove_dupes(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set()
        while node is not None:
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

    def remove_dupes_single_pointer(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set({node.data})
        while node.next is not None:
            if node.next.data in seen_data:
                node.next = node.next.next
            else:
                seen_data.add(node.next.data)
                node = node.next

    def remove_dupes_in_place(self):
        curr = self.head
        while curr is not None:
            runner = curr
            while runner.next is not None:
                if runner.next.data == curr.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next
