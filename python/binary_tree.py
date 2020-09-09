class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:

    def __init__(self):
        """A tree only has a root attribute with type Node."""
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(node.right, value)

    def find(self, value):
        if self.root is None:
            return None
        else:
            return self._find(self.root, value)

    def _find(self, node, value):
        if value == node.value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    @staticmethod
    def min_node(node):
        current = node
        while current is not None and current.left is not None:
            current = current.left
        return current

    def remove(self, value):
        if self.root is None:
            return
        if self.root.value == value:
            self.root = None
            return
        return self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = Tree.min_node(node.right)
            node.value = temp.value
            node.right = self._remove(node.right, temp.value)
        return node

    def __del__(self):
        self.root = None
        print(f'Tree deleted.')

    def __str__(self):
        if self.root is not None:
            return self._construct_str(self.root)
        return ''

    def _construct_str(self, node, to_return=None):
        if to_return is None:
            to_return = ''
        if node is not None:
            left_node_str = self._construct_str(node.left, to_return)
            current_node_str = f'{node.value} \n'
            right_node_str = self._construct_str(node.right, to_return)
            to_return = left_node_str + current_node_str + right_node_str
        return to_return


if __name__ == '__main__':
    tree = Tree()
    tree.add(5)
    tree.add(2)
    tree.add(-4)
    tree.add(0)
    tree.add(9)

    # print(tree.find(2).value)
    # print(tree.find(-4).value)
    print(tree)
    print()

    tree.remove(0)
    print(tree)
    # print(tree)
