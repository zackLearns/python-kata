class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self, initial_values=None):
        if initial_values is None:
            self.head = None
        else:
            for value in initial_values:
                self.add_last(value)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def add_after(self, target_value, value):
        new_node = Node(value)
        if self.head is None:
            raise Exception('LinkedList is empty and cannot perform add_after function.')

        current_node = self.head
        while current_node is not None:
            if current_node.value == target_value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        raise ValueError('No node matches target_node passed in.')

    def add_before(self, target_value, value):
        if self.head is None:
            raise Exception('LinkedList does not contain target_node passed in for add_after function.')
        new_node = Node(value)
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.value == target_value:
                new_node.next = previous_node.next
                previous_node.next = new_node
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError('LinkedList does not contain target_node passed in for add_before function.')

    def remove(self, value):
        if self.head is None:
            raise Exception('LinkedList is empty and cannot perform remove_node function.')

        previous_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

    def __str__(self):
        to_return = '['
        current_node = self.head
        while current_node is not None:
            to_return += f'{current_node.value}'
            current_node = current_node.next
            to_return += ', ' if current_node is not None else ''
        to_return += ']'
        return to_return


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_last(5)
    linked_list.add_last(9)
    linked_list.add_last(0)
    linked_list.add_last(-9)
    linked_list.add_last(89)
    print(linked_list)
    linked_list.remove(0)
    print(linked_list)
