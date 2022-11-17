# Finding the middle node in a linked list overview
# Interview Question #7
#
# Suppose we have a standard linked list. Construct an in-place (without extra memory)
# algorithm that's able to find the middle node!

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head
        i = 0
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
            i += 1
            print("counting of iterartion",i)
            print("fp data", fast_pointer.data)
            print("sp data", slow_pointer.data)

        return slow_pointer.data

    def insert(self, data):
        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node


if __name__ == "__main__":
    linkedlist = LinkedList()
    for i in range(10):
        linkedlist.insert(i)
    linkedlist.traverse_list()
    print("\nfinding the middle element")
    print(linkedlist.get_middle_node())
