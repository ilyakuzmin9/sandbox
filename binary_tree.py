import random




class NodeTree:
    def __init__(self, a_value):
        self.value = a_value
        self.left = None
        self.right = None


class TreeBinary:
    def __init__(self, a_root_value):
        self.root = NodeTree(a_root_value)
        # self.node = None

    def insert(self, a_insert_value):
        if self.root.value is None:
            self.root.value = a_insert_value

        elif a_insert_value < self.root.value:
            if self.root.left is None:
                self.root.left = NodeTree(a_insert_value)
            else:
                self._insert(a_insert_value, self.root)
        elif a_insert_value > self.root.value:
            if self.root.right is None:
                self.root.right = NodeTree(a_insert_value)
            else:
                self._insert(a_insert_value, self.root)

    def _insert(self, _a_insert_value, _a_node):
        if _a_insert_value < _a_node.value:
            if _a_node.left is None:
                _a_node.left = NodeTree(_a_insert_value)
            else:
                self._insert(_a_insert_value, _a_node.left)
        else:
            if _a_node.right is None:
                _a_node.right = NodeTree(_a_insert_value)
            else:
                self._insert(_a_insert_value, _a_node.right)


        # elif a_insert_value > self.root.value:
        #     if self.root.right is None:
        #         self.root.right = NodeTree(a_insert_value)
        #     else:
        #         self.root.right.insert(a_insert_value)


tree = TreeBinary(8)
# tree.insert(4)
# tree.insert(9)
# tree.insert(5)
# tree.insert(10)
# tree.insert(1)


for i in range(100):
    x = random.randint(0, 100)
    tree.insert(x)


print('done')
