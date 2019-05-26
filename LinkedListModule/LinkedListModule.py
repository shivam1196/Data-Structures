from Node import Node


class LinkedListModule:
    def __init__(self):
        self.head = None

    def insert_node_at_end(self, value):
        if self.head is None:
            self.head = Node(value)
            self.head.next = None

        else:
            head_value = self.head
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            node = Node(value)
            node.next = None
            temp.next = node

    def print_out_linked_list(self):

        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insert_data_at_head(self, value):
        if self.head is None:
            node = Node(value)
            node.next = self.head

        else:
            node = Node(value)
            node.next = self.head
            self.head = node


linked_list_module = LinkedListModule()

linked_list_module.insert_node_at_end(2)
linked_list_module.insert_data_at_head(14)
linked_list_module.print_out_linked_list()
