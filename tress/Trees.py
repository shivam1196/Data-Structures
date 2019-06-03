from TreeNode import TreeNode
from tress.stacks.Stacks import Stacks


class Trees:
    def __init__(self, value):
        self.root = TreeNode(value)

    def get_root(self):
        return self.root

    def pre_order_traversal(self):
        visited_nodes = []
        value_temp = self.root
        print (value_temp.data)

        stacks = Stacks()
        stacks.push_to_stack(value_temp)

        while value_temp is not None :

            if value_temp.has_left_child(value_temp) and not value_temp.get_is_left_visited():
                value_temp.set_is_left_visited(True)

                value_temp = value_temp.get_left_child()
                stacks.push_to_stack(value_temp)
            elif value_temp.has_right_child(value_temp) and not value_temp.get_is_right_visited():
                value_temp.set_is_right_visited(True)

                value_temp = value_temp.get_right_child()
                stacks.push_to_stack(value_temp)
                visited_nodes.append(value_temp)

            else:
                stack_pop = stacks.pop_from_stack()
                if stack_pop is not None:
                    print(stack_pop.value.data, "is the value of stack")
                    value_temp = stacks.get_top_element()


if __name__ == "__main__":
    trees = Trees("Shivam")
    root = trees.get_root()
    root.set_left_child(TreeNode("Srivastav"))
    root.get_left_child().set_left_child(TreeNode("Spring"))
    root.get_left_child().get_left_child().set_left_child(TreeNode("Python"))
    root.set_right_child(TreeNode("Android"))

    trees.pre_order_traversal()
