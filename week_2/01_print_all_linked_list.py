class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node


class LinkedList():
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):

        if self.head is None:  # head값이 none일때, 예외처리
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_all()
print(linked_list.head.next)
