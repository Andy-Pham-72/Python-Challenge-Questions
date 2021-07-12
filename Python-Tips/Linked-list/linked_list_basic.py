class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.head = Node(1)

    second = Node(2)
    third = Node(3)

    linked_list.head.next = second
    second.next = third 

    print(linked_list.head.next.next.item)