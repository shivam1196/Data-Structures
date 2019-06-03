from tress.stacks.linkedlist.Node import Node


class Stacks:
    def __init__(self):
        self.stack_size = 0
        self.head = None

    def push_to_stack(self, value):
        self.stack_size += 1
        if self.head is None:
            self.head = Node(value)


        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp

    def pop_from_stack(self):
        self.stack_size -= 1

        if self.stack_size > 0:
            stack_node = self.head
            self.head = self.head.next
            return stack_node
        else:
            return None

    def print_stack_elements(self):
        temp = self.head

        while temp is not None:
            print temp.value
            temp = temp.next


    def get_top_element(self):
        if self.stack_size > 0:
            return self.head.value
        else:
            return None


#
# if __name__ == "__main__":
#     stacks = Stacks()
#
#     stacks.push_to_stack(3)
#
#     stacks.push_to_stack(4)
#
#     stacks.print_stack_elements()
