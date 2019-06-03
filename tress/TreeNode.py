class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_right_visited = False
        self.is_left_visited = False

    def set_right_child(self, node):
        self.right = node

    def set_left_child(self, node):
        self.left = node

    def has_left_child(self, node):
        if node.left is not None:
            return True
        else:
            return False

    def has_right_child(self, node):
        if node.right is not None:
            return True
        else:
            return False

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_is_right_visited(self,value):
        self.is_right_visited = value

    def set_is_left_visited(self,value):
        self.is_left_visited = value

    def get_is_left_visited(self):
        return self.is_left_visited

    def get_is_right_visited(self):
        return  self.is_right_visited