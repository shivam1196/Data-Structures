class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_linked_list(node):
        current_node = node

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


def create_linked_list(elements):
    head = Node(elements[0])
    temp = head

    for i in range(1, len(elements)):
        element = Node(elements[i])
        temp.next = element
        temp = temp.next

    return head


node = Node

head = create_linked_list([1,2,3,4,5])

node.print_linked_list(head)
