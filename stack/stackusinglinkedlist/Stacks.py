from Node import Node


class Stacks:

    def __init__(self):
        self.stacks = None
        self.stack_size = 0

    def push(self, value):
        self.stack_size = self.stack_size+1
        if self.stacks is None:
            self.stacks = Node(value)
            self.stacks.next = None


        elif (self.stacks is not None):
            node = Node(value)
            temp = self.stacks

            self.stacks = node
            node.next = temp

    def print_all_values(self):
        tempNode = self.stacks

        while (tempNode is not None):
            print (tempNode.value)
            tempNode = tempNode.next

    def pop_elements(self):
        if(self.stack_size is not 0):
         self.stack_size = self.stack_size-1
         result = self.stacks
         self.stacks = self.stacks.next
         return result.value

        else:
            self.stack_size = self.stack_size - 1
            print "Stack is Empty"

    def get_stack_size(self):
        print ("Stack size is: ",self.stack_size)


stacks = Stacks()

stacks.push(2)

stacks.push(43)

stacks.push(100)

stacks.get_stack_size()

stacks.pop_elements()

stacks.get_stack_size()

stacks.pop_elements()
stacks.pop_elements()
stacks.pop_elements()
